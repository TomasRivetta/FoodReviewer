from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Mensaje(models.Model):
    _emisor = models.ForeignKey(User, on_delete=models.CASCADE)
    receptor = models.CharField(max_length=10)
    asunto = models.CharField(max_length= 80)
    content = models.CharField(max_length=500)
    creadoFecha = models.DateTimeField(auto_now_add=True)






