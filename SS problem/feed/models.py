from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class FriendList(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="User1")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="User2")
    
    class Meta:
        unique_together=[['user1', 'user2']]

    def __str__(self):
        return  self.user1.username    + '-' + self.user2.username    

class Chat(models.Model):
    friendship = models.ForeignKey(FriendList, on_delete=models.CASCADE, related_name="friendship")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    date = models.DateTimeField(default=datetime.now, blank=True)
    text = models.TextField(null=True, blank=False)
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return str(self.id) + '-' + self.friendship.user1.username    + '-' + self.friendship.user2.username + '-' + self.sender.username   

class Room(models.Model):
    friendship1 = models.ForeignKey(FriendList, on_delete=models.CASCADE, related_name="friendship1")
    friendship2 = models.ForeignKey(FriendList, on_delete=models.CASCADE, related_name="friendship2")

    class Meta:
        unique_together=[['friendship1', 'friendship2']]

    def __str__(self):
        return str(self.id) + '-' + self.friendship1.user1.username    + '-' + self.friendship1.user2.username + '-' + self.friendship2.user1.username    + '-' + self.friendship2.user2.username    
