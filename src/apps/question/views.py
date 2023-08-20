from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import status

from .models import Question
from .serializers import BaseQuestionSerializer, CreateQuestionSerializer, UpdateQuestionSerializer, AnswerSerializer
from .services import QuestionService
from apps.core import mixins as custom_mixins


@extend_schema(tags=['question'])
class QuestionViewSet(custom_mixins.SerializeByActionMixin,
                      custom_mixins.UpdateModelMixin,
                      custom_mixins.RetrieveModelMixin,
                      custom_mixins.CreateModelMixin,
                      custom_mixins.DestroyModelMixin,
                      GenericViewSet):
    serializer_class = BaseQuestionSerializer
    service = QuestionService()
    permission_classes = [IsAuthenticated, ]
    queryset = Question.objects.all()

    serialize_by_action = {
        'retrieve': BaseQuestionSerializer,
        'create': CreateQuestionSerializer,
        'partial_update': UpdateQuestionSerializer,
        'send_answer': AnswerSerializer,
        'get_answer': None,
        'destroy': None,
    }

    http_method_names = ['get', 'patch', 'put', 'post', 'delete']

    def perform_create(self, **kwargs):
        return self.service.create(user=self.request.user, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        obj = self.service.get_by_id(user=self.request.user, **kwargs)
        serializer = self.get_serializer(instance=obj)

        return Response(serializer.data)

    def perform_update(self, **kwargs):
        return self.service.update(user=self.request.user, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.service.delete(user=self.request.user, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=["POST"], detail=True, url_path='send_answer')
    def send_answer(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        answer = self.service.make_answer(
            user=self.request.user,
            pk=kwargs.pop('pk'),
            **serializer.data,
        )
        return Response(status=status.HTTP_200_OK, data=answer)

    @action(methods=["GET"], detail=True, url_path='get_answer')
    def get_answer(self, request, **kwargs):
        answer = self.service.get_answer(
            user=self.request.user,
            pk=kwargs.pop('pk')
        )
        return Response(status=status.HTTP_200_OK, data=answer)
