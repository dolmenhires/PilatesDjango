from djongo import models
from actividades.models import Actividad
from profesores.models import Profesor

class Clase(models.Model):
    _id = models.ObjectIdField()
    id_actividad = models.CharField(max_length=100)
    id_profesor = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    online = models.BooleanField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    lunes = models.BooleanField()
    martes = models.BooleanField()
    miercoles = models.BooleanField()
    jueves = models.BooleanField()
    viernes = models.BooleanField()
    sabado = models.BooleanField()
    domingo = models.BooleanField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    maximo_alumnos = models.IntegerField()
    maximo_alumnos_online = models.IntegerField()
    objects = models.DjongoManager()
    
    class Meta:
        db_table = 'clases'

    def __str__(self):
        return self._id