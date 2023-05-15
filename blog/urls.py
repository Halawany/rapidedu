from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='post_home'),
    path('post/<slug:slug>/', views.BlogDetailView.as_view(), name='post_detail'),
]
