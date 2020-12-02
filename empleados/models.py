from django.db import models
from areas.models import Area
from managers.models import Manager
# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    puesto = models.CharField(max_length=100)

    area_designada = models.OneToOneField(Area, null=True, blank=True, on_delete=models.CASCADE)

    managers_asignados = models.ManyToManyField(Manager, related_name='managers')

    def __str__(self):
        return self.nombre