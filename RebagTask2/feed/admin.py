from django.contrib import admin

from feed.models import GiftCard, Order, OrderHistory, UserGiftCard

# Register your models here.

class GiftCardAdmin(admin.ModelAdmin):
    pass

admin.site.register(GiftCard, GiftCardAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Order, OrderAdmin)

class OrderHistoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(OrderHistory, OrderHistoryAdmin)

class UserGiftCardAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserGiftCard, UserGiftCardAdmin)