from django.core.validators import validate_email
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.authentication.models import User


class BaseUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField()

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'username',
            'image',
        ]


class UpdateUserSerializer(BaseUserSerializer):

    class Meta(BaseUserSerializer.Meta):
        pass


class RetrieveUserSerializer(BaseUserSerializer):

    class Meta(BaseUserSerializer.Meta):
        pass


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=200,
        min_length=8,
        write_only=True
    )
    email = serializers.CharField(max_length=200, required=False)

    class Meta(BaseUserSerializer.Meta):
        fields = list(BaseUserSerializer.Meta.fields)
        fields.append('password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def validate_email(self, value):
        """
        Проверка на корректность email и дополнительная проверка, если нужно.
        """
        try:
            validate_email(value)
            return value
        except ValidationError:
            raise serializers.ValidationError("Invalid email address")