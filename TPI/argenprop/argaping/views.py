from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from argaping.business import load_db

# Create your views here.
def index(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())


def request_page(request):
    if(request.GET.get('btnBuscar')):
        load_db()
    return render(request,'load_data.html')

"""def load_data(request):
    template = loader.get_template('load_data.html')
    return HttpResponse(template.render())"""