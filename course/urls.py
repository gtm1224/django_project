from django.urls import path
from django.views.generic import TemplateView
from .views import CourseHome,CourseListView,CourseCreateView

app_name = 'course'
urlpatterns = [
    path('', CourseHome.as_view(), name='home'),
    path('course-list/',CourseListView.as_view(),name='course_list'),
    path('course-create/', CourseCreateView.as_view(), name='course_create'),
]