from django.db import models


# Create your models here.
class Services(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    duracion = models.DurationField()
