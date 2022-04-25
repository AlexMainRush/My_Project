from rest_framework import serializers
from ..models import CreateUser


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateUser
        fields = '__all__'
