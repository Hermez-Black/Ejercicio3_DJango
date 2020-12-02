from django.db import models
# from empleados.models import Empleado
# Create your models here.
class Manager(models.Model):
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    edad = models.IntegerField()
    experiencia = models.CharField(max_length=100)

    # empleados = models.ForeignKey(Empleado, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre