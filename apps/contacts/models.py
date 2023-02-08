from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class AddressBook(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    address_book = models.ForeignKey(to=AddressBook, on_delete=models.CASCADE)