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
    precio = models.IntegerField(null=False)
    calle = models.CharField(max_length=250)
    nro = models.CharField(max_length=6)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)
    def __str__(self):
        return self.calle + " " + self.nro

class Filtro(models.Model):
    id_filtro = models.IntegerField(primary_key=True)
    nombre = models.CharField(null=False, max_length=250)
    def __str__(self):
        return self.nombre