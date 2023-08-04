from rest_framework import serializers

from .models import Question


class BaseQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = [
            'id',
            'name',
            'text',
            'answers',
        ]
