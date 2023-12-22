# blog/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Post

# Create your views here.
class PostView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'posts.html', context)
    
class PostViewDetails(View):
    def get(self, request, post_id, *args, **kwargs):
        post = get_object_or_404(Post, pk=post_id)
        context = {
            'post': post
        }
        return render(request, 'post_details.html', context)