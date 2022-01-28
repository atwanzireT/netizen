from django.urls import path, re_path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('edit/<int:pk>/', UpdatePostView.as_view(), name='editPost'),
    path('addpost/', AddPostView, name='addpost'),
    path('postDetail/<int:pk>/', postDetail, name='postDetail'),
]