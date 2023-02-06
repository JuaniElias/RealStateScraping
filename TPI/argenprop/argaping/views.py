from django.shortcuts import render
from argaping.business import load_db
from argaping.models import Propiedad, Barrio


# Create your views here.

def index(request):
    # load_db()
    prop_list = Propiedad.objects.all()
    context = {'output': prop_list}
    # TODO: Listar las propiedades del barrio que se selecciona en el mapa y mostrar los calculos
    # TODO: Hacer funcionar el botón de filtro alquiler o venta
    if request.GET.get('btnReloadDB'):
        load_db()
    return render(request, 'argaping/load_data.html', context)
