from django.shortcuts import render

from clientes.models import Cliente


# Create your views here.
def add_cliente(request):
    if request.method == 'POST':
        newClient = Cliente(nombre=request.POST.get('nombre'), apellidos=request.POST.get('apellidos'),
                            dni=request.POST.get('dni'), email=request.POST.get('email'))
        print(newClient)
        newClient.save()
    return render(request, "add_cliente.html")