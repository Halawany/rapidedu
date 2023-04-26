from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView

class HomeView(CreateView):
    template_name = 'courses/home.html'