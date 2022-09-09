from django.db import models


# Create your models here.
class Socio(models.Model):
    id_socio = models.IntegerField(primary_key=True)
    dni = models.IntegerField(unique=True, null=False)
    nombre = models.CharField(max_length=250, null=False)
    apellido = models.CharField(max_length=250, null=False)
