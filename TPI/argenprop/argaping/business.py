from bs4 import BeautifulSoup
import requests
# TODO: Acomodar que el precio quede corregido con el punto y la coma para convertirlo a decimal (hay que usar locale)
import locale

from argaping.models import Propiedad, Barrio


# TODO: (Opcional) Buscar y cargar las coordenadas de los dptos cuando se hace el scraping en Nominatim.com
def load_db():
    # TODO: Hacer scraping de alquileres Y venta tambien
    url = "https://www.argenprop.com/departamento-alquiler-partido-rosario"
    # Manda la GET request
    f = requests.get(url=url)
    # Parsing
    doc = BeautifulSoup(f.text, "html.parser")
    # FindAll
    info_propiedades = doc.findAll("div", {"class": "card__monetary-values"})

    Propiedad.objects.all().delete()

    for info in info_propiedades:
        precio = float(info.find("span", {"class": "card__currency"}).next_sibling.text.strip())
        # Direccion viene con el barrio despues de la coma ("Alberdi al 600, Centro"), el split [0] trae solo la
        # direccion
        # TODO: editar direccion para que no aparezca ALQUILER
        direccion = info.find("h2", {"class": "card__address"}).next_element.strip().split(",", 1)[0]
        moneda = "ARS" if info.find("span", {"class": "card__currency"}).next_element.strip() == "$" \
            else info.find("span", {"class": "card__currency"}).next_element.strip()
        nombre_barrio = \
            info.find("p", {"class": "card__title--primary show-mobile"}).next_element.strip().split(",", 1)[0]

        barrio_actual = Barrio.objects.get_or_create(nombre=nombre_barrio)[0]

        propiedad_actual = Propiedad(precio=precio, direccion=direccion, moneda=moneda)
        propiedad_actual.barrio = barrio_actual
        propiedad_actual.save()
