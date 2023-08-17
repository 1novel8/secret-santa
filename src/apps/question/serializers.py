from rest_framework import serializers

from .models import Question


class BaseQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = [
            'id',
            'name',
            'text',
        ]


class CreateQuestionSerializer(BaseQuestionSerializer):
    party_id = serializers.IntegerField(required=True)

    class Meta(BaseQuestionSerializer.Meta):
        model = BaseQuestionSerializer.Meta.model
        fields = list(BaseQuestionSerializer.Meta.fields)
        fields.append("party_id")


class UpdateQuestionSerializer(BaseQuestionSerializer):
    class Meta(BaseQuestionSerializer.Meta):
        pass
