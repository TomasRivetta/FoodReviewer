from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.forms import ModelForm
from .models import Mensaje

class MensajeForm(forms.Form):
    receptor = forms.CharField(max_length=15)
    asunto = forms.CharField()
    mensaje = forms.CharField()

    class Meta:
        model = Mensaje
        fields = '__all__'