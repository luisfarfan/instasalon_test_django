from django.db import models

# Create your models here.
from common.models import BaseModelPerson
from rooms.models import Rooms
from services.models import Services


class Professional(BaseModelPerson):
    activo = models.BooleanField()
    services = models.ManyToManyField(Services, through='ProfessionalService')


class ProfessionalService(models.Model):
    profesional = models.ForeignKey(Professional, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    rooms = models.ManyToManyField(Rooms, through='ProfessionalServiceRoom')


class ProfessionalServiceRoom(models.Model):
    profesional_service = models.ForeignKey(ProfessionalService, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
