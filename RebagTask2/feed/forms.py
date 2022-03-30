from django import forms
from feed.models import Order, GiftCard, OrderHistory, UserGiftCard

class UserGiftCardForm(forms.ModelForm):
    class Meta:
        model = UserGiftCard
        fields = "__all__"
class GiftCardForm(forms.ModelForm):
    class Meta:
        model = GiftCard
        fields = "__all__"

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"

class OrderHistoryForm(forms.ModelForm):
    class Meta:
        model = OrderHistory
        fields = "__all__"