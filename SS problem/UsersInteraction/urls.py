"""UsersInteraction URL Configuration

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
from feed.views import HomePage, Home, get_search, search_user, add_friend, chat_messages, get_message, see_profile
from django.conf.urls import include, url 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_search, name="homePage"),
    path("search_user/<str:text>", search_user, name="search_user"),
    path("search_user/<str:username>/add", add_friend, name="add_friend"),
    # path("search_user/<str:username>", change_text, name="change_text"),
    # path('home/', Home.as_view(), name="home"),
    path('chat/<int:pk>', chat_messages, name = "chat_messages"),
    path('get_message/<int:pk>', get_message, name = "get_message"),
    path('see_profile/<int:pk>', see_profile, name = "see_profile"),
    path('accounts/', include('allauth.urls')),
    url('', include("allauth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)