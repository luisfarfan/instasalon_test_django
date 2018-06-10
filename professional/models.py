from django.db import models

# Create your models here.
from common.models import BaseModelPerson
from services.models import Services


class Professional(BaseModelPerson):
    activo = models.BooleanField()
    services = models.ManyToManyField(Services, through='ProfessionalService')


class ProfessionalService(models.Model):
    profesional = models.ForeignKey(Professional, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
