from django.db import models
from django.utils import timezone


class TipoProducto(models.Model):
    descripción = models.CharField(max_length=30)

    def __str__(self):
        return self.descripción

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    tamaño = models.TextField()
    tipoproducto = models.ForeignKey(
                        'TipoProducto'
                        ,on_delete=models.CASCADE,)

    def __str__(self):
        return self.nombre

class TipoComercio(models.Model):
    descripción = models.CharField(max_length=30)

    def __str__(self):
        return self.descripción

class Empresa(models.Model):
    nombre = models.CharField(max_length=50)
    CIF = models.CharField(max_length=15)
    teléfono = models.CharField(max_length=30)
    dirección = models.CharField(max_length=150)
    ubicación = models.TextField()
    añoIncorporación = models.IntegerField()
    tipocomercio = models.ForeignKey(
                        'TipoComercio'
                        ,on_delete=models.CASCADE,)
    producto = models.ManyToManyField(Producto)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    teléfono = models.CharField(max_length=30)
    dirección = models.CharField(max_length=150)
    email = models.EmailField()
    ubicación = models.TextField()

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    descripción = models.CharField(max_length=30)
    fecha = models.DateField()
    cliente = models.ForeignKey(
                        'Cliente'
                        ,on_delete=models.CASCADE,)
    productos = models.ManyToManyField(Producto)

    def __str__(self):
        return str(self.id)






