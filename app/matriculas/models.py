from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from djongo import models
from django.core.validators import URLValidator


class Matricula(models.Model):
    _id = models.ObjectIdField()
    id_alumno = models.CharField(max_length=100)
    id_clase = models.CharField(max_length=100)
    fecha_matricula = models.DateTimeField()
    numero_clases = models.IntegerField()
    objects = models.DjongoManager()
    
    class Meta:
        db_table = 'matriclulas'
