from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from djongo import models
from django.core.validators import URLValidator


class Actividad(models.Model):
    _id = models.ObjectIdField()
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    objects = models.DjongoManager()
    
    class Meta:
        db_table = 'actividades'

    def __str__(self):
        return self._id
