"""GESCI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Users.views import HomePage, UserEditView, PasswordChange, Classes, ProfileDetailView, edit_post, course_detail, show_course_detail,  users_profile, add_post, delete_post, students_in_group, search_course 
from django.conf.urls import include, url 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name="home"),
    path("profile/", UserEditView.as_view(), name="detail"),
    path("classes/<str:name>/", Classes.as_view(), name="classes"),
    path("password/", PasswordChange.as_view(), name="password_change"),
    path("my_profile/", ProfileDetailView.as_view(), name="my_profile"),
    path("course_detail/<int:pk>", show_course_detail, name="course_detail"),
    path("course/", course_detail, name="student_courses"),
    path("form_course/<int:pk>", edit_post, name="form_course"),
    path("users_profile/<int:pk>", users_profile, name="users_profile"),
    path("add_info/<int:pk>", add_post, name="add_post"),
    path("delete_info/<int:pk>", delete_post, name="delete_post"),
    path("group/<int:gn>", students_in_group, name="students_in_group"),
    path("search_course/<x>", search_course, name="search_course"),
    url('', include("allauth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)