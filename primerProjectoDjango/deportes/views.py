from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.forms import modelform_factory

from deportes.models import Jugador


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


JugadorForm = modelform_factory(Jugador, exclude=[])

def listar_jugadores(request):
    lista_jugadores = Jugador.objects.all()
    if request.method == 'GET':
        if request.GET.get('id') is not None:
            jugador = Jugador.objects.filter(pk=request.GET.get('id')).delete()
            return HttpResponseRedirect('/deportes/jugadores')
        if request.GET.get('orderby') is not None:
            lista_jugadores = Jugador.objects.all().order_by(request.GET.get('orderby')).values()

    if request.method == 'POST':
        if request.POST.get('action') == 'filtrar':
            nacionalidad = request.POST.get('nacionalidad_filtro')
            posicion = request.POST.get('posicion_filtro')
            if nacionalidad != "":
                lista_jugadores = Jugador.objects.filter(nacionalidad=nacionalidad)
            if posicion != "":
                lista_jugadores = Jugador.objects.filter(posicion=posicion)

    contexto = {"listado_jugadores": lista_jugadores, "listado_posiciones": ["del", "def", "port", "med"],
                "listado_nacionalidades": ["esp", "ger", "bra", "fra"]}
    return render(request, "listado_jugadores.html", contexto)

def add_jugador(request):
    mensaje = ""
    id = None
    jugador_form = JugadorForm()
    if request.method == 'POST':
        try:
            if request.POST.get('id') != 'None':
                print("eenenen")
                Jugador.objects.filter(pk=request.POST.get('id')).update(
                    nombre=request.POST.get('nombre'), equipo=request.POST.get('equipo'),
                    nacionalidad=request.POST.get('nacionalidad'), edad=request.POST.get('edad'),
                    posicion=request.POST.get('posicion'))
                mensaje = "Jugador Actualizado"
            else:
                JugadorForm(request.POST).save()
                mensaje = "Jugador Guardado"
        except Exception as e:
            mensaje = "Error al guardar"
            print(e)
    elif request.method == 'GET':
        id = request.GET.get('id')
        if id is not None:
            jugador = Jugador.objects.get(pk=id)
            jugador_form = JugadorForm(instance=jugador)
    context = {"mensaje": mensaje, "jugador_form": jugador_form, "id": id}
    return render(request, "add_jugador.html", context)