from django.shortcuts import render
from argaping.business import load_db, load_json
import json


# Create your views here.
def index(request):
    if request.GET.get('btnReloadDB'):
        load_db()

    data_alquiler = load_json("alquiler")
    data_venta = load_json("venta")

    data_alquiler_json = json.dumps(data_alquiler)
    data_venta_json = json.dumps(data_venta)

    context = {"data_alquiler_json": data_alquiler_json,
               "data_venta_json": data_venta_json}

    return render(request, 'argaping/load_data.html', context=context)
