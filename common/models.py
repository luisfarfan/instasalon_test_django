from django.db import models


class BaseModelPerson(models.Model):
    """
    Modelo Base para los modelos que se quiera guardar su auditoria
    Usage::
        from common.models import BaseModelAuditoria
        class Usuario(BaseModelAuditoria):
            usuario = models.CharField(max_length=20)
            other_fields = models.CharField(max_length=20)
    """

    # le pongo esta anotacion `%(app_label)s_%(class)s_usr_created` ya que las llaves foraneas, crean un identificador
    # por el cual se podra acceder a la relación, entonces la anotación que puse en related_name
    # la crea dinamicamente segun el modelo
    # si es que no se le pone, todos los modelos que implementan de `BaseModelAuditoria` tendrian el mismo identificador
    # y por lo tanto cuando se hagan las migraciones, saldria ERROR!
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=200)
    apellido_materno = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    edad = models.SmallIntegerField()
    usr_fecha_creacion = models.DateTimeField(auto_now_add=True)
    usr_fecha_edicion = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
