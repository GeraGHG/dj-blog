# blog/urls.py
from django.urls import path
from .views import PostListView, PostDetailView

app_name = 'blog'  # Agrega esta línea para definir el app_name
urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('<int:post_id>', PostDetailView.as_view(), name='post_details'),
]
