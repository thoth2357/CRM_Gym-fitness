from django.contrib.auth.models import AbstractBaseUser,    BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):

  def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        fullname = extra_fields['fullname'],
        email=email,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now, 
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, fullname, **extra_fields):
    return self._create_user(email, password, False, False, fullname, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    user=self._create_user(email, password, True, True, fullname='admin', **extra_fields)
    user.save(using=self._db)
    return user


class User(AbstractBaseUser, PermissionsMixin):
    fullname = models.CharField(max_length=250, default=None, null=True)
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

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
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=80)
    dni = models.CharField(max_length=9, unique=True)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=9)
    rol = models.CharField(choices=ROLES, max_length=8)

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellidos)


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
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
    
    
