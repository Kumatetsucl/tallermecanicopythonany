from django.db import models
from django.db import connection

# Create your models here.
# Modelo para CATEGORIA


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True,
                                  verbose_name='idUser')
    rut = models.CharField(max_length=12,
                           verbose_name='Rut')
    userName = models.CharField(max_length=50,
                                verbose_name='Nombre Usuario')
    nombre = models.CharField(max_length=50,
                              verbose_name='nombre')
    contrasena = models.CharField(max_length=50,
                                  verbose_name='Contraseña')
    direccion = models.CharField(max_length=80,
                                 verbose_name='Direccion')

    def __str__(self):
        return self.userName


class Cotizacion(models.Model):
    id_cotizacion = models.AutoField(primary_key=True,
                                     verbose_name='id Cotizacion')
    nombre = models.CharField(max_length=80,
                              verbose_name='Nombre Cliente')
    telefono = models.IntegerField(verbose_name='Fono Cliente')
    
    rut = models.CharField(max_length=12,
                           verbose_name='Rut')
    
    correo = models.CharField(max_length=80,
                              verbose_name='Correo')
    mensaje = models.TextField(max_length=255,
                               verbose_name='Mensaje Cotizacion')
    estado = models.CharField(max_length=80,
                              verbose_name='Estado Cotizacion',
                              default='Sin Revisar')

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True,
                                     verbose_name='id producto')
    nombreProducto = models.CharField(max_length=80,
                              verbose_name='Nombre Producto')
    marcaProducto = models.CharField(max_length=80,
                              verbose_name='Marca Producto')
    Precio = models.IntegerField(verbose_name='Precio')
    
    foto = models.ImageField(upload_to='core/img/', default='core/img/logobueno.png')
    
    favorito = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombreProducto
    
class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True, verbose_name='id Compra')
    Precio_total = models.IntegerField(verbose_name='precio Total')

    def __str__(self):
        return str(self.id_compra)
    
class Detalle_compra(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    cantidad_producto = models.IntegerField(verbose_name='Cantidad Productos')
    precio_total = models.IntegerField(verbose_name='Precio Total')

    def __str__(self):
        return f"Detalle {self.id}"
    
