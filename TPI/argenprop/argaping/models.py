from django.db import models
from django.db.models import Avg, Max, Min, Count
from django.db.models.functions import Round


# Create your models here.

class Barrio(models.Model):
    nombre = models.CharField(null=False, blank=False, max_length=250, unique=True)

    def __str__(self):
        return self.nombre


class Propiedad(models.Model):
    class Meta:
        verbose_name_plural = 'Propiedades'

    direccion = models.CharField(max_length=250)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)
    moneda = models.CharField(max_length=5)
    precio_ars = models.DecimalField(max_digits=18, decimal_places=2, null=False)
    precio_usd = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    tipo_operacion = models.CharField(max_length=15)

    def __str__(self):
        return self.direccion

    def get_barrio(self):
        return self.barrio

    @classmethod
    def get_data_barrios(cls, operacion: str):
        precio = 'precio_usd' if operacion == 'venta' else 'precio_ars'
        return list(Propiedad.objects.all().values("barrio__nombre").filter(tipo_operacion=operacion) \
                    .annotate(average=Round(Avg(precio)), maximo=Max(precio), minimo=Min(precio)
                              , cantidad=Count('id')))


class Filtro(models.Model):
    nombre = models.CharField(null=False, blank=False, max_length=250)

    def __str__(self):
        return self.nombre
