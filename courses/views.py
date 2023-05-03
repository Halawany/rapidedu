from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView

from .models import Course

class HomeView(TemplateView):
    template_name = 'courses/homepage.html'

class CoursesListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'courses/courses.html'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'