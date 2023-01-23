from bs4 import BeautifulSoup
import requests
from argaping.models import Propiedad

url = "https://www.argenprop.com/departamento-alquiler-partido-rosario"
# Manda la GET request
f = requests.get(url=url)
# Parsing
doc = BeautifulSoup(f.text, "html.parser")
# FindAll
info_propiedades = doc.findAll("div", {"class": "card__monetary-values"})

for info in info_propiedades:
    precio = info.find("span", {"class": "card__currency"}).next_sibling.text.strip()
    direccion = info.find("h2", {"class": "card__address"}).next_element.strip().split(",", 1)[0]
    moneda = "ARS" if info.find("span", {"class": "card__currency"}).next_element.strip() == "$" \
                    else info.find("span", {"class": "card__currency"}).next_element.strip()
    barrio = info.find("p", {"class": "card__title--primary show-mobile"}).next_element.strip().split(",", 1)[0]
    Propiedad.objects.create(precio=precio, direccion=direccion, barrio=barrio, moneda=moneda)
