# blog/urls.py
from django.urls import path
from .views import PostView, PostViewDetails

app_name = 'blog'  # Agrega esta línea para definir el app_name
urlpatterns = [
    path('', PostView.as_view(), name='posts'),
    path('<int:post_id>', PostViewDetails.as_view()),
]
