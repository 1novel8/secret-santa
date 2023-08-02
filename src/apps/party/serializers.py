from rest_framework import serializers

from .models import Party


class BasePartySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField(required=False)

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
