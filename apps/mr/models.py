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
        print(json.dumps(model_to_dict(self)))
        return json.dumps(model_to_dict(self))
