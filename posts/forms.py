from dataclasses import field
from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category','title', 'details', 'image')

    widgets = {
        'category': forms.TextInput(attrs={'class': 'form-control'}),
        'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title of the Post'}),
    }