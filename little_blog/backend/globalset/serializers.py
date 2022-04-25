from rest_framework import serializers
from .models import GlobalSet


class GlobalSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalSet
        fields = '__all__'
