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
    queryset = Question.objects.all()
    serializer_class = BaseQuestionSerializer
    service = QuestionService()

    http_method_names = ['get', 'patch', 'put', 'post', 'delete']
