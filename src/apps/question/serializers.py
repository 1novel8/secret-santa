from rest_framework import serializers

from .models import Question


class BaseQuestionSerializer(serializers.ModelSerializer):
    party_id = serializers.IntegerField(required=True, write_only=True)

    class Meta:
        model = Question
        fields = [
            'id',
            'name',
            'text',
            'party_id',
        ]

