from django.contrib import admin

from feed.models import ContactBook

# Register your models here.
class ContactBookAdmin(admin.ModelAdmin):
    pass

admin.site.register(ContactBook, ContactBookAdmin)