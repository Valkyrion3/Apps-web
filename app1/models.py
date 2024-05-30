from django.db import models

# Create your models here.
class pan(models.Model):
    sabor = models.CharField(max_length = 60, blank=True, null=True)
    precio = models.FloatField(null = True)
    nombre = models.CharField(max_length = 80, blank = True, null = True)
    activo = models.BooleanField(null = False, blank = False, default = False)
