from django.db import models

# Create your models here.
class Moto(models.Model):
    # crear los campors del modelo, un campo corresponde con una columna de la tabla "principal_piso"
    nombreVendedor = models.CharField(max_length=20,unique=True)
    correo = models.EmailField()
    telefono = models.CharField(max_length=9)
    precio = models.FloatField()
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=15)
    imagenMoto = models.ImageField(verbose_name="Imagen de moto",null=True,blank=True,upload_to="imgMotos")
    localidad = models.CharField(max_length=80)
    fechaFabricacion = models.DateField()
    kilometros = models.IntegerField()
    fechaCreacion = models.DateField(auto_now_add=True)
    fechaModificacion = models.DateField(auto_now=True)

    # Funcion que devuelve los valores escogidos de la clase Piso
    def __str__(self):
        return self.nombreVendedor
    
    class Meta:
        ordering = ["marca","localidad"]
