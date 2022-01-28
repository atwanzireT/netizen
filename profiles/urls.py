from django.urls import path
from .views import *

urlpatterns = [
    path('register', UserRegistrationView.as_view(), name = "register"),
    path('logout', logout_func, name='logout'),
]
