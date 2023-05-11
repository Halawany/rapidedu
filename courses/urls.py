from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('courses', views.CoursesListView.as_view(), name='courses'),
    path('course/<slug:slug>', views.CourseDetailView.as_view(), name='course_detail'),
    path('enroll/<int:pk>/', views.enroll, name='enroll'),
    path('enrolled/', views.EnrolledCourses.as_view(), name='enrolled_courses'),
    path('course/<slug:slug>/classroom', views.ClassroomView.as_view(), name='classroom'),
    path('chatbot/', views.chatbot, name='chatbot'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
