from django.shortcuts import render
from argaping.business import load_db
from argaping.models import Propiedad, Barrio


# Create your views here.

def index(request):
    # load_db()
    prop_list = Propiedad.objects.all()
    context = {'output': prop_list}
    # TODO: Ver como dibujar los barrios en el mapa
    # TODO: Listar las propiedades del barrio que se selecciona en el mapa y mostrar los calculos
    return render(request, 'argaping/load_data.html', context)
