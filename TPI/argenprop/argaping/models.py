from django.db import models


# Create your models here.

class Barrio(models.Model):
    id_barrio = models.IntegerField(primary_key=True)
    nombre = models.CharField(null=False, max_length=250)

    def __str__(self):
        return self.nombre


class Propiedad(models.Model):
    class Meta:
        verbose_name_plural = 'Propiedades'

    id_prop = models.IntegerField(primary_key=True)
    direccion = models.CharField(max_length=250)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)
    moneda = models.CharField(max_length=5)
    precio = models.IntegerField(null=False)

    def __str__(self):
        return self.calle + " " + self.nro


class Filtro(models.Model):
    id_filtro = models.IntegerField(primary_key=True)
    nombre = models.CharField(null=False, max_length=250)

    def __str__(self):
        return self.nombre
