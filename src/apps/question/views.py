from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import status

from .models import Question
from .serializers import BaseQuestionSerializer
from .services import QuestionService
from apps.core import mixins as custom_mixins


class QuestionViewSet(custom_mixins.UpdateModelMixin,
                      custom_mixins.RetrieveModelMixin,
                      custom_mixins.CreateModelMixin,
                      custom_mixins.DestroyModelMixin,
                      GenericViewSet):
    serializer_class = BaseQuestionSerializer
    service = QuestionService()
    permission_classes = [IsAuthenticated, ]
    queryset = Question.objects.all()

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
