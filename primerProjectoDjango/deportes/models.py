from django.db import models

# Create your models here.
class Seleccion(models.Model):
    nombre = models.CharField(max_length=30)
    continente = models.CharField(max_length=30)
    mundiales_ganados = models.IntegerField(max_length=3)

    def __str__(self):
        return f"{self.nombre} {self.continente} {self.mundiales_ganados}"


class Jugador(models.Model):
    nombre = models.CharField(max_length=30)
    equipo = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=30)
    edad = models.IntegerField(max_length=2)
    posicion = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.pk} {self.nombre} {self.equipo} {self.nacionalidad} {self.edad} {self.posicion}"

    def update_data(self, data):
        self.nombre = data.nombre
        self.equipo = data.equipo
        self.nacionalidad = data.nacionalidad
        self.edad = data.edad
        self.posicion = data.posicion