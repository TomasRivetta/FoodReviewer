from django.http import HttpResponse
from django.shortcuts import render, redirect
from blog.forms import UserRegisterForm, LoginForm, UserEditForm, AvatarForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Avatar, Posteo
from .forms import PosteoForm

from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

def inicio(request):
    return render(request,"blog/inicio.html",{'imagen':obtenerAvatar(request)})

def nosotros(request):
    return render(request, "blog/acerca-de.html",{'imagen':obtenerAvatar(request)})

def blog(request):
    posteos = Posteo.objects.all().order_by('-id')
    return render(request, "blog/blog.html",{'posteos':posteos})

####### LOGIN #######
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = request.POST["username"]
            clave = request.POST["password"]

            user = authenticate(username=usuario,password=clave)
            if user is not None:
                login(request, user)
                return render(request, "blog/inicio.html", {'mensaje':f'Bienvenido { user } a FoodReviewers', 'imagen':obtenerAvatar(request)})
            else:
                return render(request, "blog/login.html", {'form':form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "blog/login.html", {'form':form, "mensaje":"FORMULARIO INVALIDO"})
    else:
        form=AuthenticationForm()
        return render(request, "blog/login.html", {'form':form,"imagen":obtenerAvatar(request)})


####### REGISTRAR #######

def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]

            form.save()
            return render(request, 'blog/inicio.html', {'mensaje':f"Usuario { username } creado"})
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form':form,"imagen":obtenerAvatar(request)})


######## LOGOUT ##########

######## EDITAR USER ##########
@login_required
def editarPerfil(request):

    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():

            info = form.cleaned_data

            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]
            usuario.email = info["email"]
            usuario.password1 = info["password1"]
            usuario.password2 = info["password2"]
            usuario.comidaFavorita = info["comidaFavorita"]
            usuario.localidad = info["localidad"]
            usuario.descripcion = info["descripcion"]

            usuario.save()
            return render(request, 'blog/inicio.html', {'mensaje':f'{ usuario } logro editar su perfil con exito '})
    else:
        form = UserEditForm(instance = usuario)
    return render(request, 'blog/editarPerfil.html', {'form':form, 'usuario':usuario,"imagen":obtenerAvatar(request)})
    


def obtenerAvatar(request):
    lista = Avatar.objects.filter(user=request.user.id)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen= ""
    return imagen

@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if(len(avatarViejo)>0):
                avatarViejo.delete()
            avatar=Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'blog/inicio.html', {'usuario':request.user, 'mensaje':'Se agrego el avatar Exitosamente', "imagen":obtenerAvatar(request)})
    else:
        formulario=AvatarForm()
    return render(request, 'blog/agregarAvatar.html', {'form':formulario, 'usuario':request.user, "imagen":obtenerAvatar(request)})

@login_required
def misPublicaciones(request):
    posteos = Posteo.objects.filter(autor=request.user)
    return render(request, 'blog/misPublicaciones.html',{"posteos":posteos,"imagen":obtenerAvatar(request)})


class verPublicacion(DetailView):

    model = Posteo
    template_name = "blog/verPublicacion.html"  


@login_required
def subir_post(request):
    posteo = Posteo()

    if request.method  == "POST":
        form = PosteoForm(request.POST, instance= posteo)
        if form.is_valid():
            form.save()

            return redirect('blog')
    else:
        form = PosteoForm(instance = posteo) 

    return render(request,'blog/crearPublicacion.html', {'posteo':posteo, 'form':form,"imagen":obtenerAvatar(request)})        



'''
def login_manual(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return render(request,'blog/inicio.html',{'form':form})
    else:
        form = LoginForm()
    return render(request, "blog/login.html", {'form':form})
'''