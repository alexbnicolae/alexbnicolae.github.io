from django.db import models
from django.core.validators import RegexValidator

class ContactBook(models.Model):
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")

    first_name = models.CharField(max_length=30, verbose_name = "first name")
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    phoneNumber = models.CharField(validators= [phoneNumberRegex], max_length=10, unique=True, verbose_name = "Phone Number")

    def __str__(self):
        return  self.first_name + " " + self.last_name
    
