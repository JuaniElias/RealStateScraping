from django.shortcuts import render
from argaping.business import load_db
from argaping.models import Propiedad, Barrio


# Create your views here.

def index(request):
    # load_db()
    prop_list = Propiedad.objects.all()
    context = {'output': prop_list}
    return render(request, 'argaping/load_data.html', context)

