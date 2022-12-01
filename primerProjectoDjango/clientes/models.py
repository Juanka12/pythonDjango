from django.db import models


# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    dni = models.CharField(max_length=9)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} {self.nombre} {self.apellidos} {self.dni} {self.email}"


class Coche(models.Model):
    matricula = models.CharField(max_length=13)
    marca = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    combustible = models.CharField(max_length=30)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} {self.matricula} {self.marca} {self.color} {self.combustible} {self.cliente.dni}"
