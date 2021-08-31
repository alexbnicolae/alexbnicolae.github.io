from django import template
from feed.models import FriendList, Chat, Room
from django.http.response import FileResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, DetailView, ListView
from django.contrib.auth.models import User
from itertools import chain
from datetime import datetime
from django.shortcuts import get_object_or_404
from .forms import AddPostForm
class HomePage(TemplateView):
    http_method_names = ["get"]
    template_name = "homepage.html"

class Home(TemplateView):
    http_method_names = ["get"]
    template_name = "home.html"

def get_search(request):
    template = "home.html"
    if request.method == "POST":
        search_user = request.POST['search']
        return redirect('/search_user/' + search_user)

    my_friends = FriendList.objects.none()
    room_chat = Room.objects.none()
    if request.user.is_authenticated:
        my_friends = FriendList.objects.filter(user1 = request.user)

        for mf in my_friends:
            if FriendList.objects.filter(user1 = mf.user2, user2 = request.user).exists():
                mf2 = FriendList.objects.get(user1 = mf.user2, user2 = request.user)
                if Room.objects.filter(friendship1 = mf, friendship2 = mf2).exists() == False:
                    Room.objects.create(friendship1 = mf, friendship2 = mf2)

        room_chat = Room.objects.filter(friendship1__user1 = request.user)
    
    context = {
        'my_friends':my_friends,
        'room_chat':room_chat,
    }

    return render(request, template, context)

def chat_messages(request, pk):
    try:
        if request.method == "POST":
            search_user = request.POST['search']
            return redirect('/search_user/' + search_user)
    except Exception as e:
        pass

    template = "chat_messages.html"
    room_chat = Room.objects.get(id = pk)

    my_chat_friend1 = Chat.objects.filter(friendship = room_chat.friendship1)
    my_chat_friend2 = Chat.objects.filter(friendship = room_chat.friendship2)

    my_chat_friend = my_chat_friend1|my_chat_friend2
    my_chat_friend = my_chat_friend.order_by("-date")

    if request.method == "POST":
        new_message = Chat.objects.create(friendship = room_chat.friendship1, sender = request.user,text = request.POST.get("text"))
        
    context = {
        'room_chat': room_chat,
        'my_chat_friend': my_chat_friend, 
    }
    return render(request, template, context)

def get_message (request, pk):
    template = "chat_messages.html"
    friend_chat = FriendList.objects.get(id = pk)
    
    context = {
        
    }
    return render(request, template, context, content_type="application/html")

def see_profile(request, pk):
    try:
        if request.method == "POST":
            search_user = request.POST['search']
            return redirect('/search_user/' + search_user)
    except Exception as e:
        pass
    template = "profile.html"
    profile = get_object_or_404(User, id=pk)
    you_add = FriendList.objects.filter(user1 = request.user, user2=profile).exists()
    context = {
        'profile': profile,
        'you_add': you_add,
    }
    return render(request, template, context)

def search_user(request, text):
    template = "search_user.html"
    if request.method == "POST":
        search_user = request.POST['search']
        return redirect('/search_user/' + search_user)

    user = User.objects.filter(username__contains=text) 
    fname = User.objects.filter(first_name__contains=text) 
    lname = User.objects.filter(last_name__contains=text)

    users = user|fname|lname

    query_friend_list = Room.objects.none()
    for u in users:
        fl = Room.objects.filter(friendship1__user1 = request.user, friendship1__user2  = u, friendship2__user1 = u, friendship2__user2 = request.user)
        query_friend_list = query_friend_list|fl
    
    context = {
        'users': users,
        'text': text,
        'query_friend_list': query_friend_list,
    }   
    return render(request, template, context)

def add_friend(request, username):
    data = request.POST.dict()
    if "action" not in data or "username" not in data:
        return HttpResponseBadRequest("Missing data")

    try:
        other_user = User.objects.get(username = data['username'])
    except User.DoesNotExist:
        return HttpResponseBadRequest("Missing user")

    if data['action'] == "Add Friend":
        follower = FriendList.objects.get_or_create(
            user1 = request.user,
            user2 = other_user,
        )
    else:
        try:
            follower = FriendList.objects.get(
                user1 = request.user,
                user2 = other_user,
            )
        except FriendList.DoesNotExist:
            follower = None

        if follower:
            follower.delete()

    return JsonResponse({
        'succes':True,
        'wording': "Unfriend" if data['action'] == "Add Friend" else "Add Friend",
    })

    
