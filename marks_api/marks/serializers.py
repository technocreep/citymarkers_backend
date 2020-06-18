from rest_framework import serializers
from .models import Mark


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'latti',
            'longi',
            'author',
            'addrdate',
            'photo',
            'status',
            'typeof',
        )
        model = Mark
