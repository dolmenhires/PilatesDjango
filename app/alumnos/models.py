from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from djongo import models
from django.core.validators import URLValidator


class Alumno(models.Model):
    _id = models.ObjectIdField()
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateTimeField()
    direccion = models.CharField(max_length=100)
    cp = models.CharField(max_length=5)
    localidad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    movil = models.CharField(max_length=10)
    mail = models.EmailField()
    forma_pago = models.CharField(max_length=100)
    fecha_inicio = models.DateTimeField()
    fecha_matricula_fin = models.DateTimeField()
    pago_matricula = models.BooleanField()
    cantidad = models.FloatField()
    estudio_postural = models.BooleanField()
    dolencias_patologias = models.CharField(max_length=800)
    yoga = models.BooleanField()
    pilates = models.BooleanField()
    hipopresivos = models.BooleanField()
    yoga_infantil = models.BooleanField()
    pilates_infantil = models.BooleanField()
    mamas_bebes = models.BooleanField()
    charlas_educa = models.BooleanField()
    charlas_bebes = models.BooleanField()
    taller_meditacion = models.BooleanField()
    mindfulness = models.BooleanField()
    proteccion_datos = models.BooleanField()
    archivo_firmado = models.BooleanField()
    otros = models.CharField(max_length=250)
    objects = models.DjongoManager()
    
    class Meta:
        db_table = 'alumnos'

