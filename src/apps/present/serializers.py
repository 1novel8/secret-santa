from rest_framework import serializers

from .models import Present


class BasePresentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Present
        exclude = ('deleted_at', )
