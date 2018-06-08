from django.db import models

# Create your models here.
from services.models import Services


class Rooms(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    ubigeo = models.CharField(max_length=6)
