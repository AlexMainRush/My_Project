from django.db import models
from garpix_page.models import BasePage
from .tag import Tag


class PostPage(BasePage):
    title_111 = models.CharField(max_length=100, verbose_name='Заголовок поста', null=True)
    description = models.CharField(max_length=220, verbose_name='Краткое описание поста', null=True)
    text = models.TextField(verbose_name='Текст поста', null=True)
    img = models.ImageField(verbose_name='Изображение', null=True)
    tags = models.ManyToManyField(Tag, verbose_name='Теги', related_name='tag_posts', blank=True)
    template = "pages/post.html"

    def get_serializer(self):
        from ..serializers import PostPageSerializer
        return PostPageSerializer

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ("-created_at",)
