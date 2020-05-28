from django.db import models

# Create your models here.
class Libro(models.Model):
    Titulo = models.CharField(max_length=40)
    Autor = models.CharField(max_length=45)
    Edicion = models.CharField(max_length=45)
    Editorial = models.CharField(max_length=45)
    Fecha = models.DateField()
    NumPaginas = models.PositiveIntegerField()


   def FichaBibliografica(self):
        cadena = "{0}, {1}, {2}, {3}, {4}"
        return cadena.format(self.Autor,self.Titulo,self.Fecha,self.Editorial,self.NumPaginas)

    def __str__(self):
        return self.FichaBibliografica()