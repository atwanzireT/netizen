from http.client import HTTPResponse
from django.shortcuts import render
from django.views import generic
from .models import *
from .forms import *
from .forms import PostForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.
def AddPostView(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method =='POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()  #save data to table
            form = PostForm
            messages.success(request,"Your Post has been posted. Thank you for your post.")
            return HttpResponseRedirect('/article/addpost/')
    category = Category.objects.all()
    form = PostForm
    context={'form':form, 'category':category  }
    return render(request, 'add_post.html', context)  


class UpdatePostView(generic.UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = PostForm

def postDetail(required, pk):
    post = Post.objects.get(pk = pk)
    postlist = Post.objects.all()[:3]
    context = {
        'post':post,
        'postlist':postlist,
    }
    return render(required, "postDetails.html", context)
