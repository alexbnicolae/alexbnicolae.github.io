from feed.models import FriendList
from django.contrib import admin
from .models import FriendList, Chat, Room

class FriendListAdmmin(admin.ModelAdmin):
    pass
admin.site.register(FriendList, FriendListAdmmin)

class ChatAdmin(admin.ModelAdmin):
    pass
admin.site.register(Chat, ChatAdmin)

class RoomAdmin(admin.ModelAdmin):
    pass
admin.site.register(Room, RoomAdmin)