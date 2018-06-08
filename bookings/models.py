from django.db import models

# Create your models here.
from professional.models import ProfessionalServiceRoom
from users.models import Users


class Bookings(models.Model):
    fecha = models.DateTimeField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    profesional_service_room = models.ForeignKey(ProfessionalServiceRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
