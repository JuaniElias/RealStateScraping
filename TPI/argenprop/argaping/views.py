from django.http import JsonResponse
from django.shortcuts import render
from argaping.business import load_db, load_json
import json
from decimal import Decimal


# Create your views here.

# TODO: Hacer que al clickear cada barrio aparezca su info.
# TODO: (Opcional) Mostrar la info del barrio en un Popper de esos.


def index(request):
    # load_db()
    promedios_alquiler = load_json("alquiler", "precio_ars")
    promedios_venta = load_json("venta", "precio_usd")

    promedios = {'promedios_alquiler': promedios_alquiler, 'promedios_venta': promedios_venta}
    # TODO: Mostrar cálculos. Promedios de alquiler y venta. Si no se encontrara uno de los dos mostrar mensaje acorde.
    # TODO: Recordar que solo vamos a mostrar aquellos barrios que tienen más de 5 propiedades en la DB.
    if request.GET.get('btnReloadDB'):
        pass
        # load_db()
        # load_json()

    promedios_alquiler_json = json.dumps(promedios_alquiler)
    print(type(promedios_alquiler_json))
    return render(request, 'argaping/load_data.html', {"promedios_alquiler_json": promedios_alquiler_json})
