from django.db import models

# Create your models here.
from professional.models import ProfessionalService
from services.models import Services


class Rooms(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    ubigeo = models.CharField(max_length=6)
    professionalservices = models.ManyToManyField(ProfessionalService, through='RoomProfessionalService')


class RoomProfessionalService(models.Model):
    profesional_service = models.ForeignKey(ProfessionalService, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
