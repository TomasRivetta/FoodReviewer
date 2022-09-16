from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(label="Nombre",widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label="Apellido",widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    comidaFavorita = forms.CharField(label='Comida favorita', widget=forms.TextInput(attrs={'class':'form-control'}))
    localidad= forms.CharField(label='Localidad',widget=forms.TextInput(attrs={'class':'form-control'}))
    descripcion = forms.CharField(label='Descripcion',widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2','comidaFavorita','localidad','descripcion']
        help_texts = {k:" " for k in fields}

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'



class LoginForm(forms.ModelForm):

    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password= forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['email','password']

    def clean(self):

        email = self.cleaned_data['email']  
        password = self.cleaned_data['password']  

        if not authenticate(email= email, password= password):
            raise forms.ValidationError("El email o contraseña son incorrectos")


class UserEditForm(UserCreationForm):
    last_name = forms.CharField(label="Modificar nombre",widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label="Modificar apellido",widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(label="Modifical E-Mail",widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    comidaFavorita = forms.CharField(label='Comida favorita', widget=forms.TextInput(attrs={'class':'form-control'}))
    localidad= forms.CharField(label='Localidad',widget=forms.TextInput(attrs={'class':'form-control'}))
    descripcion = forms.CharField(label='Descripcion',widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['last_name','first_name','email', 'password1', 'password2','comidaFavorita','localidad','descripcion']
        help_texts = {k:" " for k in fields}

class AvatarForm(forms.Form):
    imagen = forms.ImageField(label="Imagen")