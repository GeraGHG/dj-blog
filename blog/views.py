# blog/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Post

# Create your views here.
# https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-display/
'''
class PostListView(ListView): revisar el modelo ListView
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
'''
class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'posts.html', context)

'''
class PostDetailView(DetailView):  revisar el modelo DetailView
    model = Post
    template_name = 'post_details.html'
    context_object_name = 'post'
'''
    
class PostDetailView(View):
    def get(self, request, post_id, *args, **kwargs):
        post = get_object_or_404(Post, pk=post_id)
        context = {
            'post': post
        }
        return render(request, 'post_details.html', context)