from django.db import models

# Create your models here.


class Project(models.Model):
    programa = models.CharField(max_length=40)
    solicitante = models.CharField(max_length=100)
    documento_solicitante = models.CharField(max_length=15)
    representante = models.CharField(max_length=100)
    documento_representante = models.CharField(max_length=15)
    correo_representante = models.CharField(max_length=10)

    #esto aprece en la parte de administracion para que en lugar de project aparezca proyectos
    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    # este soliciting aparece en la parte de administracion como solicitante
    def __str__(self):
        return self.solicitante
