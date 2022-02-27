import json
from django.shortcuts import get_object_or_404, render
from django.contrib import messages


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from feed.models import ContactBook
from feed.serializers import ContactBookSerializer

@csrf_exempt
def contactBook_list(request):
    if request.method == "GET":
        contactBook = ContactBook.objects.all()
        serializer = ContactBookSerializer(contactBook, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ContactBookSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            messages.add_message(request, messages.SUCCESS, 'Your contact was successfully added.')
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def contactBook_detail(request, pk):
    try:
        contactBook = ContactBook.objects.get(pk=pk)
    except ContactBook.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == "GET":
        serializer = ContactBookSerializer(contactBook)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ContactBookSerializer(contactBook, data=data)
        if serializer.is_valid():
            serializer.save()
            messages.add_message(request, messages.INFO, 'Your contact was successfully edited.')
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        contactBook.delete()
        messages.add_message(request, messages.WARNING, 'Your contact was successfully deleted.')
        return HttpResponse(status=204)


def home_page(request):
    template = "homepage.html"
    contacts = ContactBook.objects.all()
    context = {
        'contacts': contacts,
    }
    return render (request, template, context)
    
def info_contact(request, pk):
    template = "info_contact.html"
    get_contact = ContactBook.objects.get(id=pk)
    context = {
        'get_contact': get_contact,
    }
    return render (request, template, context)

def add_contact(request):
    template = "add_contact.html"
    form = ContactBookSerializer()
    context ={
        'form': form,
    }
    return render(request, template, context)

def edit_contact(request, pk):
    template = "edit_contact.html"
    contact = get_object_or_404(ContactBook, id=pk)
    context = {
        'contact':contact,
    }
    return render (request, template, context)