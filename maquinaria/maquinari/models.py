from django.db import models

# Create your models here.
class Maquinaria(models.Model):
    Descripcion = models.CharField(max_length=130, unique=True)
    Cantidad = models.CharField(max_length=200)


    def __str__(self):
        return "{}".format(self.Descripcion)

    class Meta:
        verbose_name = "Maquinaria"
        verbose_name_plural = "Maquinaria"
        ordering = ('Descripcion',)

