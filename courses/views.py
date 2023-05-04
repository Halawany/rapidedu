from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.http import JsonResponse
# from .chat import get_response

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


# def predict(request):
#     if request.method == 'POST':
#         text = request.POST.get('message')
#         response = get_response(text)
#         message = {"answer": response}
#         return JsonResponse(message)
#     else:
#         return JsonResponse({'error': 'Invalid request method'})