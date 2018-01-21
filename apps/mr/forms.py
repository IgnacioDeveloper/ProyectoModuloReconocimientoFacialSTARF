from django import forms
from apps.mr.models import Alumno, Usuario

class AlumnoForm(forms.ModelForm):

    class Meta:
        model = Alumno
        fields=[
            #'id',
            'legajo',
            'nombre',
            'apellido',
            'mail',
        ]
        labels = {
            #'id':'Id',
            'legajo':'Legajo',
            'nombre':'Nombre',
            'apellido':'Apellido',
            'mail':'Mail'
        }
        widgets = {
            #'id': forms.TextInput(attrs={'class':'form-control'}),
            'legajo': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'mail': forms.EmailInput(attrs={'class':'form-control'}),
        }

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields=[
            'codigo_usuario',
            'nombre',
            'apellido',
            'username',
            'password',
            'tipo',
        ]
        labels = {
            'codigo_usuario':'Codigo de Usuario',
            'nombre':'Nombres',
            'apellido':'Apellidos',
            'username':'Username',
            'password':'Password',
            'tipo':'Tipo'
        }
        widgets = {
            'codigo_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.TextInput(attrs={'class':'form-control'}),
            'tipo':forms.Select(attrs={'class':'form-control'},choices=(('1','Bedel'),('2','Director'))),
        }