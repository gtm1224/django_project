from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Course

class CourseHome(TemplateView):
    template_name = "course/home.html"

class UserMixin:
    def get_queryset(self):
        qs = super(UserMixin,self).get_queryset()
        return qs.filter(user=self.request.user)

class UserCourseMixin(UserMixin):
    model = Course



class CourseListView(UserCourseMixin,ListView):

    context_object_name = 'courses'
    template_name = 'course/course_list.html'