from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class HomeView(ListView):

	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'

class BlogDetailView(DetailView):

	model = Post
	template_name = 'blog/post_detail.html'