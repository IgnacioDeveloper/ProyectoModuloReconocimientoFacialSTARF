from django.db import models

class Usuario(models.Model):
    codigo_usuario = models.CharField(max_length=5)
    nombre = models.CharField(max_length = 65)
    apellido = models.CharField(max_length= 65)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=200)
    tipo = models.CharField(max_length=2)

    def __str__(self):
        return self.codigoUsuario

class Alumno(models.Model):
    legajo = models.CharField(max_length=5)
    nombre = models.CharField(max_length=65)
    apellido = models.CharField(max_length=65)
    mail = models.CharField(max_length=200)

    def __str__(self):
        return self.legajo
