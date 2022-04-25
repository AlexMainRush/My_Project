from rest_framework import serializers
from blog.models import PostPage


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPage
        fields = ('title',)
