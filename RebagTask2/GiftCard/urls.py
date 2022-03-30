"""GiftCard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path


from feed.views import home, card_list, displayCards, add_gift_card, add_order_form, order_list, order_detail, edit_order_form, get_order_history, get_order_history_template, admin_gift_card_user_post, admin_gift_card, admin_gift_card_user_edit, admin_gift_card_user_delete, admin_zone_page, admin_display_gc, admin_manipulate_a_gc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = "home"),
    path('admin_zone/', admin_zone_page, name = "admin_zone_page"),
    path('card_list/', card_list, name="card_list"),
    path('order_list/', order_list, name="order_list"),
    path('admin_gift_card_user_post/', admin_gift_card_user_post, name="admin_gift_card_user_post"),
    path('admin_gift_card_user_edit/', admin_gift_card_user_edit, name="admin_gift_card_user_edit"),
    path('admin_gift_card_user_delete/', admin_gift_card_user_delete, name="admin_gift_card_user_delete"),
    path('admin_display_gc/', admin_display_gc, name="admin_display_gc"),
    path('admin_gift_card/', admin_gift_card, name="admin_gift_card"),
    path('add_gift_card/', add_gift_card, name="add_gift_card"),
    path('admin_manipulate_a_gc/<int:pk>', admin_manipulate_a_gc, name="admin_manipulate_a_gc"),
    path('order_detail/<int:pk>', order_detail, name="order_detail"),
    path('add_order/<int:pk>', add_order_form, name="add_order_form"),
    path('edit_order/<int:pk>', edit_order_form, name="edit_order_form"),
    path('order_history/<int:pk>', get_order_history, name="get_order_history"),
    path('allOrders/<int:pk>', get_order_history_template, name="get_order_history_template"),
    path('displayCards/', displayCards, name="displayCards"),
    # path('generate_token/', generateToken, name="generateToken"),
    path('', include('allauth.urls')),
]
