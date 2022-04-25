from rest_framework import viewsets
from blog.models import PostPage
from ..serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = PostPage.objects.all()
    serializer_class = ArticleSerializer
