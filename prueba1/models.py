from django.db import models

# Create your models here.
class categoria(models.Model):
    nombre = models.CharField(max_length = 60, blank=True, null=True)
    descripcion = models.CharField(max_length = 60, blank=True, null=True)
    
class producto(models.Model):
    nombre = models.CharField(max_length = 60, blank=True, null=True)
    color = models.CharField(max_length = 60, blank=True, null=True)
    precio = models.FloatField()
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)