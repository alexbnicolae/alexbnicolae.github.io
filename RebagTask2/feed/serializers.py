from feed.models import Order, GiftCard, OrderHistory, UserGiftCard
from rest_framework import serializers


class UserGiftCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGiftCard
        fields = "__all__"

class GiftCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiftCard
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class OrderHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderHistory
        fields = "__all__"