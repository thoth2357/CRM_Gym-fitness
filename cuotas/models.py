from django.db import models

# Create your models here.
class cuotas(models.Model):
    numbre_de_la_cuotas = models.CharField("numbre_de_la_cuotas", max_length=50, default=None)
    Tipo_de_tarifa = models.CharField("Tipo_de_tarifa", max_length=50)
    numbre_de_la_tarifa = models.CharField("Tipo_de_tarifa", max_length=50)
    actividad = models.ForeignKey("clases.Clases", verbose_name="actividades para agregar para agregar", on_delete=models.CASCADE, blank=True)
    session = models.IntegerField()

    def __str__(self) -> str:
        return self.numbre_de_la_cuotas
    
