from django.shortcuts import render

# Create your views here.
def home(request):
    params = {"title": "Deportes", "description": "Una pagina de inicio de una aplicacion deportes"}
    return render(request, "home.html", params)

def listar_equipos(request):
    listado_mundial = [
        {"seleccion": "España", "continente": "Europa", "mundiales_ganados": "1"},
        {"seleccion": "Alemania", "continente": "Europa", "mundiales_ganados": "4"},
        {"seleccion": "Uruguay", "continente": "America", "mundiales_ganados": "2"},
        {"seleccion": "Argentina", "continente": "America", "mundiales_ganados": "2"},
        {"seleccion": "Japon", "continente": "Asia", "mundiales_ganados": "0"},
        {"seleccion": "Iran", "continente": "Asia", "mundiales_ganados": "0"},
    ]
    newSeleccion = None
    if request.method == 'POST':
        form = request.POST
        newSeleccion = {"seleccion": form.get('seleccion'), "continente": form.get('continente'),
                        "mundiales_ganados": form.get('mganados')}
        print(newSeleccion)
    if not newSeleccion == None:
        listado_mundial.append(newSeleccion)
    last_page = request.META.get('HTTP_REFERER')
    contexto = {"listado_equipos": listado_mundial, "last_page": last_page}
    return render(request, "listado_mundial.html", contexto)

def add_seleccion(request):
    return render(request, "add_seleccion.html")