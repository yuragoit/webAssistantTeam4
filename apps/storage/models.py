from django.contrib.auth.models import User
from django.db import models

from .сonstans import MAX_CHAR_LENGTH


# Create your models here.
class File(models.Model):
    file = models.FileField()
    name = models.CharField(max_length=MAX_CHAR_LENGTH, null=True)
    type = models.CharField(max_length=MAX_CHAR_LENGTH, null=True)
    upload_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)