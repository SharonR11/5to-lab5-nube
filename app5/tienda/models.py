from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date
# Create your models here.
class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, auto_created=True)
    nombre=models.CharField(max_length=100)
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    cantidad=models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.cantidad}"
    
class Alumno(models.Model):
    idAlumno = models.AutoField(primary_key=True, auto_created=True)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    email=models.EmailField()
    celular=models.IntegerField()
    fecha_nac=models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Estudiante(models.Model):
    idAlumno = models.AutoField(primary_key=True, auto_created=True)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    email=models.EmailField()
    celular=models.IntegerField()
    fecha_nac=models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"