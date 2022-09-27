from django.urls import path
from .views import mensajeria,enviar_mensaje,misMensajes, verMensaje


urlpatterns = [
    path("", mensajeria,name="list"),
    path("enviar_mensaje/", enviar_mensaje,name="enviar_mensaje"),
    path("misMensajes/", misMensajes, name= "mis_mensajes"),
    path("verMensaje/<pk>", verMensaje, name = "ver_mensaje"),
    ]

