from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import User
from django.views.generic import TemplateView, DetailView, ListView
from django.contrib.auth.forms import UserChangeForm
from django.views import generic
from django.urls import reverse_lazy 
from .forms import EditProfileForm


class HomePage(TemplateView):
    http_method_names = ["get"]
    template_name = "homepage.html"

class Attend(TemplateView):
    http_method_names = ["get"]
    template_name = "courses/courses.html"

class Classes(TemplateView):
    http_method_names = ["get"]
    template_name = "classes/classes.html"

class ProfileDetailView(DetailView):
    http_method_names = ["get"]
    template_name = "detail.html"
    model = User
    context_object_name = "user"
    slug_field = "username"
    slug_url_kwarg = "username"

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "detail.html"
    success_url = reverse_lazy('detail')

    def get_object(self):
        return self.request.user

