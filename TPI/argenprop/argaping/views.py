from django.shortcuts import render
from argaping.business import load_db, load_json
from argaping.models import Propiedad, Barrio


# Create your views here.

def index(request):
    # load_db()
    promedios_alquiler = load_json("alquiler", "precio_ars")
    promedios_venta = load_json("venta", "precio_usd")

    promedios = {'promedios_alquiler': promedios_alquiler, 'promedios_venta': promedios_venta}
    # TODO: Mostrar cálculos. Promedios de alquiler y venta. Si no se encontrara uno de los dos mostrar mensaje acorde.
    # TODO: Recordar que solo vamos a mostrar aquellos barrios que tienen más de 5 propiedades en la DB.
    if request.GET.get('btnReloadDB'):
        # load_db()
        load_json()
    return render(request, 'argaping/load_data.html', promedios)
