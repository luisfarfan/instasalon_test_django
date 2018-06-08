from django.db import models


# Create your models here.
from common.models import BaseModelPerson


class Users(BaseModelPerson):
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    class Meta:
        managed = True
