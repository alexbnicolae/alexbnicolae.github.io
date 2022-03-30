
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token


class GiftCard(models.Model):
    name = models.CharField(max_length=200)
    available = models.BooleanField()

    def __str__(self):
        return  f'{self.id} {self.name}'

class UserGiftCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    giftCard = models.ForeignKey(GiftCard, on_delete=models.CASCADE, related_name="giftCard")
    amount = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        unique_together=[['user', 'giftCard']]

    def __str__(self):
        return  f'{self.id} {self.user.username} {self.giftCard.name}'

class Order(models.Model):
    giftCard = models.ForeignKey(UserGiftCard, on_delete=models.CASCADE, related_name="giftCardName")
    productOrdered = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    date = models.DateTimeField()
    orderNumber = models.CharField(max_length=200)

    def __str__(self):
        return  f'{self.id} {self.giftCard.user.username} {self.giftCard.giftCard.name}'

class OrderHistory(models.Model):
    giftCard = models.ForeignKey(UserGiftCard, on_delete=models.CASCADE, related_name="giftCardName2")
    logHistory = ArrayField(ArrayField(models.CharField(max_length=200), blank=True), blank=True)

    def __str__(self):
        return  f'{self.id} {self.giftCard.user.username} {self.giftCard.giftCard.name}'

@receiver(post_save, sender=UserGiftCard)
def create_order_history(sender, instance, created, **kwargs):
    if created :
        OrderHistory.objects.create(giftCard = instance, logHistory=[]) 

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)        