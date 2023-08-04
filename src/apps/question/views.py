from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from .models import Question
from .serializers import BaseQuestionSerializer
from .services import QuestionService
from apps.core import mixins as custom_mixins


class QuestionViewSet(mixins.ListModelMixin,
                      custom_mixins.UpdateModelMixin,
                      custom_mixins.RetrieveModelMixin,
                      custom_mixins.CreateModelMixin,
                      custom_mixins.DestroyModelMixin,
                      GenericViewSet):
    serializer_class = BaseQuestionSerializer
    service = QuestionService()
    permission_classes = [IsAuthenticated, ]

    http_method_names = ['get', 'patch', 'put', 'post', 'delete']

    def get_queryset(self):
        queryset = Question.objects.filter(party_id=self.kwargs.get('party_pk'))
        return queryset

    def perform_create(self, **kwargs):
        return self.service.create(user=self.request.user, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        obj = self.service.get_by_id(user=self.request.user, **kwargs)
        serializer = self.get_serializer(instance=obj)

        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        questions = self.service.list(user=self.request.user, **kwargs)
        serializer = self.get_serializer(questions, many=True)

        return Response(serializer.data)

    def perform_update(self, **kwargs):
        return self.service.update(user=self.request.user, **kwargs)
