from rest_framework import serializers

from apps.party.models import Party
from apps.authentication.models import User
from apps.question.serializers import BaseQuestionSerializer
from apps.authentication.serializers import RetrieveUserSerializer


class BasePartySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField(required=False)
    questions = BaseQuestionSerializer(many=True, read_only=True)
    users = RetrieveUserSerializer(many=True, read_only=True)

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
            'finish_time',
        ]

    # users
    # draw_results
    # questions - M2M
    # answers - M2M


class InviteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', ]


class QuestionAnswerSerializer(serializers.Serializer):
    question_name = serializers.CharField(read_only=True)
    question_text = serializers.CharField(read_only=True)
    answer = serializers.CharField(read_only=True)


class ResultSerializer(serializers.Serializer):
    answer_list = QuestionAnswerSerializer(many=True)
    receiver = RetrieveUserSerializer()
