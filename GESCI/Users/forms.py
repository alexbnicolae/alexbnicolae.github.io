from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.forms import fields
from .models import User
from django.contrib.auth import authenticate

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')