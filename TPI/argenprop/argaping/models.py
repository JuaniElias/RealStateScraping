from django.db import models


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
    precio = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    tipo_operacion = models.CharField(max_length=15)

    def __str__(self):
        return self.direccion


class Filtro(models.Model):
    nombre = models.CharField(null=False, blank=False, max_length=250)

    def __str__(self):
        return self.nombre
