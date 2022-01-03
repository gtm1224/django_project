from django.urls import path
from django.views.generic.base import TemplateView
from .views import CourseHome,CourseListView

app_name = 'course'
urlpatterns = [
    path('', CourseHome.as_view(), name='home'),
    path('course-list/',CourseListView.as_view(),name='course_list'),
]