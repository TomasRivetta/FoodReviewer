from pyexpat import model
from django.db import models
from django.contrib.auth.models import User 


class userlog(models.Model):
    nombre=models.CharField(max_length=60)
    _contraseña=models.CharField(max_length=50)

    def __str__(self):
        return(self.nombre)



class Avatar(models.Model):   
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    imagen= models.ImageField(upload_to='avatares',null = True,blank=True)