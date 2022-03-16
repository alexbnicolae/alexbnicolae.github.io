from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from .models import User, Chat


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('friendship', 'sender', 'text', 'file',)