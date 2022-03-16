from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from feed.forms import UserCreationForm, LoginForm, ClientForm
from feed.models import Client
from django.contrib import messages


def add_client(request):
    template = "add_client.html"
    form = ClientForm()
    error = ""

    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Client Added!")
            return redirect("/")
        else:
            error = "Error"

    context = {
        'form': form,
    }

    return render(request, template, context)

def home(request):
    template = "home.html"
    users = User.objects.all()
    clients = Client.objects.all()
    context = {
        'users': users,
        'clients': clients,
    }
    return render(request, template, context)

def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Logged Out.')
    return redirect("/")

def login_view(request):
    template = "login.html"
    form = LoginForm()
    error = ""

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Logged In.')
            return redirect("/")
        else:
            error = "Invalid login"

    context = {
        'form': form,
        'error': error,
    }
    return render(request, template, context)
    
def signup_view(request):
    template = "signup.html"
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'User Added!')
                return redirect("/")
        except Exception as e:
            pass
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }

    return render(request, template, context)

