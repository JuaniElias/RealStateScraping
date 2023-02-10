from bs4 import BeautifulSoup
import requests
import locale
from decimal import Decimal
from django.db.models import Avg
from argaping.models import Propiedad, Barrio
import re
from django.core import serializers
from django.http import HttpResponse
import json


def load_db():
    # Borra las propiedades para cargarlas devuelta
    Propiedad.objects.all().delete()
    tipos_operacion = ['alquiler', 'venta']
    forbidden_words = re.compile(r"(\b)alquiler(\b)|(\b)muy(\b)|(\b)lindo(\b)|,|(\b)al (\b)|(\b)departamento(\b)",
                                 re.IGNORECASE)

    # Setea la ubicación a Argentina para formatear el string de precio bien con los puntos y la coma
    locale.setlocale(locale.LC_ALL, 'es_AR.UTF8')

    # Scrapeo del dólar inmobiliario/ladrillo para convertir los precios de las viviendas
    f = requests.get(url="https://www.bullano.com.ar/blog/dolar-inmobiliario.html#cotizacion")

    doc = BeautifulSoup(f.text, "html.parser")
    precio_dolar_actual_str = doc.find("span", {"class": "valor_dolar di"}).text.strip()
    precio_dolar_actual = Decimal(locale.atof(precio_dolar_actual_str)).quantize(Decimal("1.00"))

    for tipo in tipos_operacion:
        pagina = 1
        while True:
            url = f"https://www.argenprop.com/departamento-{tipo}-partido-rosario-pagina-{pagina}"
            pagina += 1

            # Manda la GET request, si no existe el numero de página sale del loop
            f = requests.get(url=url)
            # Parsing
            doc = BeautifulSoup(f.text, "html.parser")

            # FindAll de cada tarjeta de cada propiedad
            info_propiedades = doc.findAll("div", {"class": "card__monetary-values"})
            # Si no se encuentra una propiedad sale del loop
            if not info_propiedades:
                break
            for info in info_propiedades:
                try:
                    precio_str = info.find("span", {"class": "card__currency"}).next_sibling.text.strip()

                    # Direccion viene con el barrio despues de la coma ("Alberdi al 600, Centro"), el split [0] trae
                    # solo la direccion
                    direccion = info.find("h2", {"class": "card__address"}).next_element.strip().split(",", 1)[0]
                    direccion = forbidden_words.sub("", direccion).strip()
                    moneda = "ARS" if info.find("span", {"class": "card__currency"}).next_element.strip() == "$" \
                        else info.find("span", {"class": "card__currency"}).next_element.strip()
                    if moneda == 'ARS':
                        precio_ars = Decimal(locale.atof(precio_str)).quantize(Decimal("1.00"))
                        precio_usd = precio_ars / precio_dolar_actual
                    else:
                        precio_usd = Decimal(locale.atof(precio_str)).quantize(Decimal("1.00"))
                        precio_ars = precio_usd * precio_dolar_actual
                    nombre_barrio = \
                        info.find("p", {"class": "card__title--primary show-mobile"}).next_element.strip().split(",",
                                                                                                                 1)[0]

                    barrio_actual = Barrio.objects.get_or_create(nombre=nombre_barrio)[0]

                    propiedad_actual = Propiedad(precio_ars=precio_ars, precio_usd=precio_usd, direccion=direccion,
                                                 moneda=moneda, tipo_operacion=tipo)
                    propiedad_actual.barrio = barrio_actual
                    propiedad_actual.save()
                except AttributeError:
                    pass
    print("It's loaded!")


# TODO: Pasar JSON resultante al archivo JS.

def load_json(operacion: str, moneda: str):
    # TODO: Cambiar barrio id por barrio nombre a través de un inner join ?.
    promedios_barrio = list(Propiedad.objects.values("barrio").filter(tipo_operacion=operacion).annotate(average=Avg(moneda)))

    return promedios_barrio
