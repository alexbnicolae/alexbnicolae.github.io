from dataclasses import field
from email.policy import default
from feed.models import Client
from django.contrib import admin
from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class ClientCreationForm(forms.ModelForm):
    password = forms.CharField(max_length=25, widget=forms.PasswordInput)

    class Meta:
        model = Client
        fields = ('username', 'email')

    def save(self, commit=True):
        user = super(ClientCreationForm, self).save(commit=False)
        user.password = make_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class ClientChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Client
        fields = "__all__"

class ClientAdmin(admin.ModelAdmin):
    form = ClientChangeForm
    add_form = ClientCreationForm

    def get_form(self, request, obj = None, **kwargs):
        defaults = {}

        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)

admin.site.register(Client, ClientAdmin)