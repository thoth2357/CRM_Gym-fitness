from django.db import models

# Create your models here.
class habitaciones(models.Model):
    nombre_de_la_habitación = models.CharField("max_length=50")
    capacidad = models.IntegerField()

