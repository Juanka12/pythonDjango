from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    mensajes = {"mensaje1": "Valor mensaje1", "mensaje2": "Valor mensaje2"}
    return render(request, "bienvenido.html", mensajes)

def despedida(request):
    return render(request, "despedida.html")

def listar_datos(request):
    listado_alumnos = [
        {"nombre": "nombre1", "apellidos": "apellidos1", "dni": "dni1"},
        {"nombre": "nombre2", "apellidos": "apellidos2", "dni": "dni2"},
        {"nombre": "nombre3", "apellidos": "apellidos3", "dni": "dni3"}
    ]
    contexto = {"listado_alumnos": listado_alumnos}
    return render(request, "alumnos.html", contexto)