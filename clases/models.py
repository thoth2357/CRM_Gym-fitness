from django.db import models

# Create your models here.
class Grupo(models.Model):
    Nombre_del_grupo = models.CharField("Nombre_del_grupo", max_length=50)

    def __str__(self) -> str:
        return self.Nombre_del_grupo

class Clases(models.Model):
    grupo = models.ForeignKey("clases.Grupo", verbose_name="La clase grupal debe pertenecer a", on_delete=models.CASCADE)
    actividad = models.CharField("nombre_de_la_actividad", max_length=50)
    descripción = models.CharField("nombre_de_la_descripción", max_length=50)
    duración = models.DurationField(help_text="duración del evento")

    def __str__(self) -> str:
        return self.actividad
