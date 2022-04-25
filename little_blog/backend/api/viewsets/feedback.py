from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from ..models import Feedback
from ..serializers import FeedbackSerializer


class FeedbackViewSet(GenericViewSet, CreateModelMixin):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
