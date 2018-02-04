from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.mr.models import Alumno

class AlumnoForm(forms.ModelForm):

    class Meta:
        model = Alumno
        fields=[
            'legajo',
            'nombre',
            'apellido',
            'mail',
        ]
        labels = {
            'legajo':'Legajo',
            'nombre':'Nombre',
            'apellido':'Apellido',
            'mail':'Mail'
        }
        widgets = {
            'legajo': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'mail': forms.EmailInput(attrs={'class':'form-control'}),
        }

class UsuarioForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
                'first_name',
                'last_name',
                'username',
        ]
        labels = {
            'first_name':'Nombres',
            'last_name':'Apellidos',
            'username':'Nombre de Usuario',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
        }