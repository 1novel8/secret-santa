from rest_framework import serializers

from apps.present.models import Present


class BasePresentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField(required=False)
    url = serializers.URLField(required=False)
    is_preferred = serializers.BooleanField(required=True)

    class Meta:
        model = Present
        fields = [
            'id',
            'name',
            'description',
            'image',
            'url',
            'is_preferred',
        ]
