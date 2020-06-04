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

class Cliente(models.Model):
    Nombre = models.CharField(max_length=45)
    ApellidoPaterno = models.CharField(max_length=40)
    ApellidoMaterno = models.CharField(max_length=40)
    Domicilio = models.CharField(max_length=100)

    def NombreCompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.ApellidoPaterno,self.ApellidoMaterno,self.Nombre)
    
    def __str__(self):
        return self.NombreCompleto()
        
class Ventas(models.Model):
    Libro = models.ForeignKey(Libro, null=False, blank=False, on_delete=models.CASCADE)
    Cliente = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
    FechaVenta = models.DateTimeField(auto_now_add=True)       