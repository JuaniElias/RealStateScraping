from django.shortcuts import render
from argaping.business import load_db, test_load_barrio
from argaping.models import Propiedad, Barrio


# Create your views here.
def index(request):
    latest_barrio_list = Barrio.objects.all()
    output = ', '.join([b.nombre for b in latest_barrio_list])
    context = {'output': latest_barrio_list}
    return render(request, 'argaping/load_data.html', context)


def request_page(request):
    if request.GET.get('btnBuscar'):
        test_load_barrio()
    return render(request, 'load_data.html')


"""def load_data(request):
    template = loader.get_template('load_data.html')
    return HttpResponse(template.render())"""
