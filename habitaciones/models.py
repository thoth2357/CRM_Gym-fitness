from django.db import models

# Create your models here.
class habitaciones(models.Model):
    nombre_de_la_habitacion = models.CharField(max_length=50)
    capacidad = models.IntegerField()

    def __str__(self) -> str:
        return self.nombre_de_la_habitacion
    

