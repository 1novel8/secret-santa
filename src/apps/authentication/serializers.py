from rest_framework import serializers

from .models import User


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
        fields = list(BaseUserSerializer.Meta.fields)
        fields.append('image')


class RetrieveUserSerializer(BaseUserSerializer):
    image = serializers.ImageField()

    class Meta(BaseUserSerializer.Meta):
        pass


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=200,
        min_length=8,
        write_only=True
    )

    class Meta(BaseUserSerializer.Meta):
        fields = list(BaseUserSerializer.Meta.fields)
        fields.append('password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

