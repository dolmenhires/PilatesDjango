from djongo import models

# Create your models here.

class Profesor(models.Model):
    _id = models.ObjectIdField()
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    especialidades = models.CharField(max_length=100)
    objects = models.DjongoManager()
    
    class Meta:
        db_table = 'profesores'
