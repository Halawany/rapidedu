from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('courses', views.CoursesListView.as_view(), name='courses'),
    path('course/<slug:slug>', views.CourseDetailView.as_view(), name='course_detail'),
    # path('predict/', views.predict, name='predict'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
