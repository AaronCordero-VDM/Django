from django.db import models

# Create your models here.
class Piso(models.Model):
    # crear los campors del modelo, un campo corresponde con una columna de la tabla "principal_piso"
    numReferencia = models.CharField(max_length=20,unique=True)
    imagenPiso = models.ImageField(verbose_name="Imagen de piso",null=True,blank=True,upload_to="imgPiso")
    direccion = models.CharField(max_length=100)
    poblacion = models.CharField(max_length=80)
    precio = models.FloatField()
    metrosCuadrados = models.IntegerField()
    cp = models.CharField(max_length=10)
    planta = models.IntegerField()
    banios = models.IntegerField()
    ascensor = models.BooleanField()
    terraza = models.BooleanField()
    garaje = models.BooleanField()
    descCorta = models.CharField(max_length=200)
    comentario = models.TextField(max_length=600)
    correo = models.EmailField()
    fechaAlta = models.DateField(auto_now_add=True)
    fechaModificacion = models.DateField(auto_now=True)

    # Funcion que devuelve los valores escogidos de la clase Piso
    def __str__(self):
        return self.numReferencia
    
    class Meta:
        ordering = ["poblacion","cp"]

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    inversor = models.BooleanField()

    def __str__(self):
        return self.nombre
