from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Course
from braces.views import LoginRequiredMixin

from django.views.generic.edit import CreateView,DeleteView
from django.shortcuts import redirect
from .forms import CourseCreateForm


class CourseHome(TemplateView):
    template_name = "course/home.html"

class UserMixin:
    def get_queryset(self):
        qs = super(UserMixin,self).get_queryset()
        return qs.filter(user=self.request.user)

class UserCourseMixin(UserMixin,LoginRequiredMixin):
    model = Course
    login_url = '/account/login'



class CourseListView(UserCourseMixin,ListView):

    context_object_name = 'courses'
    template_name = 'course/course_list.html'

class CourseCreateView(UserCourseMixin,CreateView):
    fields = ['title','overview']
    template_name = 'course/course_create.html'

    def post(self,request,*args,**kwargs):
        form = CourseCreateForm(data=request.POST)
        if form.is_valid():
            new_course = form.save(commit=False)
            new_course.user = self.request.user
            new_course.save()
            return redirect('course:course_list')
        return self.render_to_response({'form':form})