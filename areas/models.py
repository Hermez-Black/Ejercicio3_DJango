from django.db import models

# Create your models here.
class Area(models.Model):
    nombre = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    dueño = models.CharField(max_length=100)


    def __str__(self):
        return self.nombre
