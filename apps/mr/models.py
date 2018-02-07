from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.forms.models import model_to_dict
from django.dispatch import receiver
import json

class Alumno(models.Model):
    legajo = models.CharField(max_length=5)
    nombre = models.CharField(max_length=65)
    apellido = models.CharField(max_length=65)
    mail = models.CharField(max_length=200)

    def __str__(self):
        return json.dumps(model_to_dict(self))

class Aula(models.Model):
    numero = models.CharField(max_length=5)
    descripcion = models.CharField(max_length=65)

    def __str__(self):
    	aula_str = 'Aula '+self.numero
    	aula_str = aula_str if len(self.descripcion) == 0 else aula_str +' ('+self.descripcion+')'
    	return aula_str

class Camara(models.Model):
	ip = models.CharField(max_length=16)
	descripcion = models.CharField(max_length=65)
	aula = models.ForeignKey(Aula, null=False, blank=False, on_delete=models.CASCADE)

	def __str__(self):
		return json.dumps(model_to_dict(self))

