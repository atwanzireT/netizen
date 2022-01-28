from django.urls import path
from .views import *

urlpatterns = [
    path('register', UserRegistrationView.as_view(), name = "register"),
    path('logout_func', logout_func, name='logout'),
]