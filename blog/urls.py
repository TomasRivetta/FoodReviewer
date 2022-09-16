from django.urls import path
from blog.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path('acerca-de/', nosotros, name="acerca-de"),
    path('iniciar-sesion/', login_request, name ='login'),
    path('editarPerfil/', editarPerfil, name ='editarPerfil'),
    path('editarPerfil/agregarAvatar', agregarAvatar, name ='agregarAvatar'),
    path('register/', register,name="register"),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name="logout"),
    path('blog/', blog,name="blog"),
    path("",inicio,name="inicio"),
]