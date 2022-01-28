from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home' ),
    path('like/', views.like_post, name = 'like_post'),
    path('category/<str:id>/', views.category, name = 'category'),
]
