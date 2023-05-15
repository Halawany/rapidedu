from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .chatbot.chat import get_response
from django.db.models import Q

from .models import Course, Enrollment, Chapter, Instructor, FrequentlyAskedQuestion

class HomeView(TemplateView):
    template_name = 'courses/homepage.html'

class CoursesListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'courses/courses.html'

class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = "courses/course_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        enrolled = Enrollment.objects.filter(user=self.request.user, course=self.object).exists()
        context['enrolled'] = enrolled
        context['instructors'] = Instructor.objects.all()
        context['faqs'] = FrequentlyAskedQuestion.objects.filter(course=self.object)
        return context
    
class EnrolledCourses(LoginRequiredMixin, ListView):
    model = Enrollment
    template_name = 'courses/enrolled_courses.html'
    context_object_name = 'enrollments'

    def get_queryset(self):
        return Enrollment.objects.filter(user=self.request.user)

class ClassroomView(LoginRequiredMixin, TemplateView):
    template_name = 'courses/classroom.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chapters'] = Chapter.objects.all()
        return context

@login_required()
def enroll(request, pk):
    course = get_object_or_404(Course, pk=pk)
    Enrollment.objects.create(user=request.user, course=course)

    return redirect('classroom', slug=course.slug)

class CourseSearchView(ListView):
    model = Course
    template_name = 'courses/search.html'
    context_object_name = 'courses'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Course.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        return object_list


def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        response = get_response(message)
        data = {
            'response': response
        }
        return JsonResponse(data)
    else:
        return render(request, 'courses/chatbot.html')