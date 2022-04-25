from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from ..models import CreateUser
from ..serializers import CreateUserSerializer
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model
User = get_user_model()


class CreateUserViewSet(GenericViewSet, CreateModelMixin):
    queryset = CreateUser.objects.all()
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        feedback = serializer.save()
        headers = self.get_success_headers(serializer.data)

        User.objects.create_user(username=feedback.name, email=feedback.email, is_active=True, is_staff=False)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
