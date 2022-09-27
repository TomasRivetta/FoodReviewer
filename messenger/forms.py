from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.forms import ModelForm
from .models import Mensaje


class MensajeForm(forms.Form):
    receptor = forms.CharField()
    asunto = forms.CharField()
    mensaje = forms.Textarea()

    class Meta:
        model = Mensaje
        fields = '__all__'