from django.db import models

# Create your models here.
from rooms.models import RoomProfessionalService
from users.models import Users


class Bookings(models.Model):
    fecha = models.DateField()
    hora_inicio = models.TimeField(null=False)
    hora_fin = models.TimeField(null=False)
    room_profesional_service = models.ForeignKey(RoomProfessionalService, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
