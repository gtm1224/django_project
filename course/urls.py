from django.urls import path
from django.views.generic.base import TemplateView
from .views import CourseHome

app_name = 'course'
urlpatterns = [
    path('', CourseHome.as_view(), name='home'),
]