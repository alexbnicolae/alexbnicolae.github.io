from django.db import models

class Client(models.Model):
    username = models.CharField(max_length=500, unique=True, verbose_name="Username")
    email = models.EmailField(max_length=500, unique=True, verbose_name="Email")
    password = models.CharField(max_length=500)

    def __str__(self):
        return  self.username 

    
