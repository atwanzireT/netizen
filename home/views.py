from django.db.models import fields
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from posts.models import *
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required

def home(request):
	user = request.user
	category = Category.objects.all().order_by('?')[:3]
	posts = Post.objects.all()
	editorsPick = Post.objects.all().order_by('?')[:2]
	latest_news = Post.objects.all()[:6]

	search = request.GET.get("search")
	if search != "" and search is not None:
		posts = Post.objects.filter(title__icontains=search) 
		return render(request, "search.html", {'posts':posts, 'user': user})

	context = {
		'user':user,
		'category':category,
		'posts':posts,
		'editorsPick': editorsPick,
		'latest_news': latest_news,
	}
	return render(request, 'index.html', context)

def like_post(request):
	return HttpResponseRedirect('/like/')

def category(request, id):
	user = request.user
	category = Post.objects.filter(category_id = id)
	category_count = Post.objects.filter(category_id = id).count()
	context = {
		'category':category,
		'user':user,
		'category_count':category_count, 
	}
	return render(request, 'category.html', context)