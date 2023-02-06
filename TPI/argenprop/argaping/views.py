from django.shortcuts import render
from argaping.business import load_db
from argaping.models import Propiedad, Barrio


# Create your views here.

def index(request):
    # load_db()
    prop_list = Propiedad.objects.all()
    context = {'output': prop_list}
    # TODO: Mostrar cálculos. Promedios de alquiler y venta. Si no se encontrara uno de los dos mostrar mensaje acorde.
    # TODO: Recordar que solo vamos a mostrar aquellos barrios que tienen más de 5 propiedades en la DB.
    if request.GET.get('btnReloadDB'):
        load_db()
    return render(request, 'argaping/load_data.html', context)
