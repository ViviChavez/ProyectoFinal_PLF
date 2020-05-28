from django.db import models

# Create your models here.
class Libro(models.Model):
    Titulo = models.CharField(max_length=40)
    Autor = models.CharField(max_length=45)
    Edicion = models.CharField(max_length=45)
    Editorial = models.CharField(max_length=45)
    Fecha = models.DateField()
    NumPaginas = models.PositiveIntegerField()
