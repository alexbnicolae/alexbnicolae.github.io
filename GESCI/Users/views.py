from django.core.checks import messages
from django.shortcuts import get_object_or_404, render, redirect
from .models import StudentGroup, Teaching, User, Attendance, Class
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordChangeView
from django.views import generic
from django.urls import reverse_lazy 
from .forms import EditProfileForm, PasswordChangingForm, ClassForm
from django.core.paginator import Paginator


class HomePage(TemplateView):
    http_method_names = ["get"]
    template_name = "home.html"

class Classes(TemplateView):
    http_method_names = ["get"]
    template_name = "classes/classes.html"

class ProfileDetailView(TemplateView):
    http_method_names = ["get"]
    template_name = "profile.html"
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        items = User.objects.all()
        groups = StudentGroup.objects.all()
        context['items'] = items
        context['groups'] = groups
        return context

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "detail.html"
    success_url = reverse_lazy('my_profile')

    def get_object(self):
        return self.request.user

class PasswordChange(PasswordChangeView):
    form_class  = PasswordChangingForm
    template_name = 'password_change.html'
    success_url = reverse_lazy('my_profile')
    

class ShowCourseDetail(TemplateView):
    http_method_names =['get']
    template_name = 'courses/course_detail.html'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        items = Class.objects.all()
        context['items'] = items
        return context
        
def course_detail(request) :
    items = Class.objects.all()
    if request.user.is_student == True:
        courses = Attendance.objects.filter(student__user__id=request.user.id)
    elif request.user.is_teacher== True:
        courses = Teaching.objects.filter(teacher__user__id=request.user.id)
    elif request.user.is_admin:
        courses = Teaching.objects.all()

    course_paginator = Paginator(courses, 1)
    page_num = request.GET.get('page')
    page = course_paginator.get_page(page_num)
    context = {
        'items' : items,
        'courses' : courses,
        'page' : page
    }
    return render(request, 'courses/courses.html', context)

def users_profile(request, pk):
    template = "users_profile.html"
    post = User.objects.get(id=pk)
    teachers = Teaching.objects.all()
    context = {'post': post, 'teachers': teachers}

    return render(request, template, context)


def show_course_detail(request, pk):
    template = "courses/course_detail.html"
    post = Class.objects.get(id=pk)
    context = {'post': post}

    return render(request, template, context)

def edit_post(request, pk):
    template = "courses/form_course.html"
    post = get_object_or_404(Class, pk=pk)

    if request.method == "POST":
        form = ClassForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                return redirect('/course_detail/'+ str(pk))
        except Exception as e:
            messages.Warning(request, "Your post was not saved due to an error {}".format(e))
    else:
        form = ClassForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


        

    
    