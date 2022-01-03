from django.shortcuts import render
from django.views.generic.base import TemplateView

class CourseHome(TemplateView):
    template_name = "course/home.html"