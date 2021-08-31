from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from .models import User, Post

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=25, widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=25, widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=25, widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

class ClassForm(forms.ModelForm):
    text =  forms.CharField(widget=forms.Textarea(attrs={'style':'border:2px solid black','class':'form-control',"rows":20, "cols":50}))
    class Meta:
        model = Post
        fields = ('text', 'file')

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('teacher', 'course', 'group', 'text', 'file',)

