from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.

class Mensaje(models.Model):
    emisor = models.ForeignKey(User,null = True ,on_delete=models.CASCADE)
    receptor = models.CharField(max_length=10)
    asunto = models.CharField(max_length= 80)
    content = models.CharField(max_length = 500)
    creadoFecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (self.asunto)





