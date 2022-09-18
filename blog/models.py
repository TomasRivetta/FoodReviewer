from pyexpat import model
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User 
from ckeditor_uploader.fields import RichTextUploadingField


class userlog(models.Model):
    nombre=models.CharField(max_length=60)
    _contraseña=models.CharField(max_length=50)

    def __str__(self):
        return(self.nombre)


class Posteo(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo', max_length=255, blank = False,null=False)
    descripcion = models.CharField('Descripcion', max_length=120, blank = False,null=False)

    contenido = RichTextUploadingField(blank=True,null=True)

    imagen = models.ImageField(blank=False,null=True, upload_to="imgposts")
    
    autor= models.ForeignKey(User, null=True ,on_delete=models.SET_NULL)
    fecha_creacion = models.DateField('Fecha de  creacion',auto_now=False,auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Posteos'

    def __str__(self):
        return(self.titulo , self.autor)

class Avatar(models.Model):   
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    imagen= models.ImageField(upload_to='avatares',null = True,blank=True)

