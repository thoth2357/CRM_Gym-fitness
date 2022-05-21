from django.db import models

TIPO_CLIENTE = (
    ("S", "SOCIO"),
    ("V", "VISITA")
)
ROLES = (
    ("1", "ROL1"),
    ("2", "ROL2")
)

# Create your models here.
class Empleado(models.Model):
    'Employee class'
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=80)
    dni = models.CharField(max_length=9, unique=True)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=9)
    rol = models.CharField(choices=ROLES, max_length=8)

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellidos)


class Cliente(models.Model):
    foto = models.ImageField(upload_to='imagenes/clientes/')
    tipo_cliente = models.CharField(choices=TIPO_CLIENTE, max_length=8)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    telefono = models.CharField(max_length=9)
    email = models.EmailField()
    dni = models.CharField(max_length=9, unique=True)
    codigo_postal = models.CharField(max_length=5)
    direccion = models.CharField(max_length=200)
    cuota = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_baja = models.DateField(null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellidos)