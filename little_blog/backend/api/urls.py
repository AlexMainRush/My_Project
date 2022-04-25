from rest_framework import routers
from .viewsets import ArticleViewSet, FeedbackViewSet, CreateUserViewSet


blog_router = routers.DefaultRouter()
blog_router.register('article', ArticleViewSet)
blog_router.register('feedback', FeedbackViewSet)
blog_router.register('create_user', CreateUserViewSet)

urlpatterns = []
urlpatterns += blog_router.urls
