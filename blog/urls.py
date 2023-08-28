from django.urls import path, include
from rest_framework import  routers
from .views import *
router = routers.SimpleRouter()
router.register(r'articles', BlogViewSet)


urlpatterns = [
    path('', HomeView.as_view(), name="articles"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name='article-delete'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='article_edit'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('api/', include(router.urls), name="register")
]