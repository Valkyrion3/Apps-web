from django.db import models

# Create your models here.
class categoria(models.Model):
    nombre = models.CharField(max_length = 60, blank=True, null=True)
    estado = models.BooleanField(null = False, blank = False, default = True)
    def save(self, *args, **kwargs):
        if self.nombre:
            self.nombre = self.nombre.upper()  # Convertir el nombre a mayúsculas
        return super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.nombre}"


class pieza(models.Model):
    nombre = models.CharField(max_length = 60, blank=True, null=True)
    color = models.CharField(max_length = 60, blank=True, null=True)
    precio = models.FloatField(null = True)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    stock = models.IntegerField()
    estado = models.BooleanField(null = False, blank = False, default = True)
    def save(self, *args, **kwargs):
        if self.nombre:
            self.nombre = self.nombre.upper()  # Convertir el nombre a mayúsculas
        if self.color:
            self.color = self.color.upper()  # Convertir el color a mayúsculas
        return super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.nombre}"

class proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    provinicia = models.CharField(max_length=100)
    estado = models.BooleanField(null = False, blank = False, default = True)
    def save(self, *args, **kwargs):
        if self.nombre:
            self.nombre = self.nombre.upper()
        if self.direccion:
            self.direccion = self.direccion.upper()
        if self.ciudad:
            self.ciudad = self.ciudad.upper()
        if self.provinicia:
            self.provinicia = self.provinicia.upper()
        return super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.nombre}"

class suministro(models.Model):
    proveedor = models.ForeignKey(proveedor, on_delete=models.CASCADE)
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(null = False, blank = False, default = True)
    def __str__(self):
        return f"Suministro {self.id}"

class suministro_pieza(models.Model):
    pieza = models.ForeignKey(pieza, on_delete=models.CASCADE)
    suministro = models.ForeignKey(suministro, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    def save(self, *args, **kwargs):
        if self.precio:
            self.subtotal = self.precio * self.cantidad  #Calcular el subtotal
        return super().save(*args, **kwargs)