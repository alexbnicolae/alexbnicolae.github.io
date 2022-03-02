from django.core.checks import messages
from django.shortcuts import get_object_or_404, render, redirect
from .models import Groups, Student, StudentGroup, TeacherCourse, Teaching, User, Attendance, Post, TeacherCourse
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordChangeView
from django.views import generic
from django.urls import reverse_lazy 
from .forms import EditProfileForm, PasswordChangingForm, ClassForm, AddPostForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError


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
        items = Post.objects.filter()
        context['items'] = items
        return context
        
def course_detail(request) :
    template = 'courses/courses.html'
    if request.method == "POST":
        searched = request.POST['searched']
        return redirect('/search_course/' + searched)

    items = Post.objects.all()
    if request.user.is_student == True:
        courses = Attendance.objects.filter(student__user__id=request.user.id)
        items = Teaching.objects.all()
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
        'page' : page,
        'a': False,
    }
    return render(request, template, context)

def users_profile(request, pk):
    template = "users_profile.html"
    post = User.objects.get(id=pk)
    users = User.objects.all()
    teachers = TeacherCourse.objects.all()
    context = {
        'post': post, 
        'teachers': teachers,
        'users': users,
        }

    return render(request, template, context)


def show_course_detail(request, pk):
    template = "courses/course_detail.html"
    course_id  = Teaching.objects.get(id=pk)
    posts = Post.objects.filter(teacher__user__id=course_id.teacher.user.id, course__name=course_id.course.name, group__number=course_id.group.number).order_by('-id')
    course_paginator = Paginator(posts, 3)
    page_num = request.GET.get('page')
    page = course_paginator.get_page(page_num)
    context = {
        'posts': posts,
        'course_id' : course_id,
        'page' : page,
        }

    return render(request, template, context)

def edit_post(request, pk):
    template = "courses/form_course.html"
    post = get_object_or_404(Post, pk=pk)
    teach = Teaching.objects.filter(teacher__user__id=request.user.id)
    if request.method == "POST":
        form = ClassForm(request.POST or None, request.FILES or None, instance=post)

        try:
            if form.is_valid():
                form.save()
                for t in teach:
                    if t.teacher == post.teacher and t.course == post.course and t.group == post.group:
                        return redirect('/course_detail/'+ str(t.id))
        except Exception as e:
            messages.Warning(request, "Your post was not saved due to an error {}".format(e))
    else:
        form = ClassForm(instance=post)

    context = {
        'form': form,
        'post': post,
        'teach': teach,
    }

    return render(request, template, context)

def add_post(request, pk):
    template = "add_post.html"
    course_id  = Teaching.objects.get(id=pk)

    if request.method == "POST":
        form = AddPostForm(request.POST or None, request.FILES or None)
        try:
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "Info Added!")
                return redirect('/course_detail/'+ str(pk))
        except Exception as e:
                messages.Warning(request, "Your post was not saved due to an error {}".format(e))
    else:
        form = AddPostForm()

    print(form.errors)
    context = {
        'form': form,
        'course_id' : course_id,
    }

    return render(request, template, context)
        
        
def delete_post(request, pk):
    post = get_object_or_404(Post, id = pk)
    post.delete()
    teach = Teaching.objects.filter(teacher__user__id=request.user.id)
    messages.add_message(request, messages.SUCCESS, "Info Deleted!")
    for t in teach:
        if t.teacher == post.teacher and t.course == post.course and t.group == post.group:
            return redirect('/course_detail/'+ str(t.id))
    
def students_in_group(request, gn):
    template = "classes.html"
    studentGroup = StudentGroup.objects.all()
    group = Groups.objects.get (number = gn)

    context = {
        'studentGroup' : studentGroup,
        'group' : group,
    }
    return render(request, template, context)


def search_course(request, x):
    template = "search_course.html"
    
    searched = x
    items = Post.objects.all()
    if request.user.is_student == True:
        courses = Attendance.objects.filter(course__name__contains=searched, student__user__id=request.user.id)
        items = Teaching.objects.all()
    elif request.user.is_teacher== True:
        courses = Teaching.objects.filter(course__name__contains=searched, teacher__user__id=request.user.id)
    elif request.user.is_admin:
        courses = Teaching.objects.filter(course__name__contains=searched)

    course_paginator = Paginator(courses, 1)
    page_num = request.GET.get('page')
    page = course_paginator.get_page(page_num)    

    context = {
        'items' : items,
        'courses' : courses,
        'page' : page,
        'searched': searched,
    }
    return render(request, template , context)