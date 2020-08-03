from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Account(AbstractUser):
    address = models.CharField(max_length=250)
    phone_number = PhoneNumberField()
