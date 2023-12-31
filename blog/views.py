from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import *
from .models import Post
from django.urls import reverse_lazy


# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-post_date']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_detailed.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    fields = ['title', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home')


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # authentication_classes = (TokenAuthentication,)

