from django.http import HttpResponse

from .models import Socio

def index(request):
    socios = Socio.objects.all()
    output = ', '.join([s.nombre + " " + s.apellido for s in socios])
    return HttpResponse(output)


def alta(request, id_socio):
    return HttpResponse(f"Alta del usuario {id_socio}")


def baja(request, id_socio):
    return HttpResponse(f"Baja del usuario {id_socio}")


def modificacion(request, id_socio):
    return HttpResponse(f"Modificación del usuario {id_socio}")
