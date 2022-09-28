from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Mensaje
from .forms import MensajeForm
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from blog.views import obtenerAvatar
from datetime import date
import datetime 
from django.http import HttpResponse


# Create your views here.

@login_required
def mensajeria(request):
    usuarios = User.objects.all()
    print(usuarios)
    return render(request,"messenger/mensajeria.html", {"usuarios":usuarios,"imagen":obtenerAvatar(request)})

    
@login_required
def enviar_mensaje(request):
    Emisor = request.user
    if request.method  == "POST":
        form = MensajeForm(request.POST,request.FILES) #ese request.files dudoso
        if form.is_valid():

            informacion = form.cleaned_data

            mensaje = Mensaje(emisor=Emisor,receptor=informacion['receptor'],asunto=informacion['asunto'],content=informacion['mensaje'])

            mensaje.save()

            mensajes = Mensaje.objects.filter(receptor=request.user)

            return render(request,'messenger/misMensajes.html',{"mensajee":"Se envio el mensaje con exito","mensajes":mensajes,"imagen":obtenerAvatar(request)})
    else:
        form = MensajeForm() 
        return render(request,'messenger/enviar_mensaje.html', {'form':form}) 


@login_required
def misMensajes(request):
    mensajes = Mensaje.objects.filter(receptor=request.user)
    return render(request, 'messenger/misMensajes.html',{"mensajes":mensajes,"imagen":obtenerAvatar(request)})
