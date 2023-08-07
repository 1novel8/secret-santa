from rest_framework import serializers

from .models import Party
from ..question.serializers import BaseQuestionSerializer


class BasePartySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField(required=False)
    questions = BaseQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Party
        fields = [
            'id',
            'name',
            'description',
            'image',
            'users',
            'draw_results',
            'questions',
        ]

    # users
    # draw_results
    # questions - M2M
    # answers - M2M
