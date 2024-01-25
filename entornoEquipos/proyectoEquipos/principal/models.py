from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Competicion(models.Model):
    # crear los campors del modelo, un campo corresponde con una columna de la tabla "principal_piso"
    nombre = models.CharField(max_length=50,unique=True,verbose_name="Nombre de la competicion")
    lugar = models.CharField(max_length=50, verbose_name="Lugar de la competicion")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    modificado = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

    # Funcion que devuelve los valores escogidos de la clase Moto
    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ["-creado"]

#########################################################################################################################################
        
class Equipo(models.Model):
    # crear los campors del modelo, un campo corresponde con una columna de la tabla "principal_piso"
    nombre = models.CharField(max_length=50,unique=True,verbose_name="Nombre del equipo")
    categoria = models.CharField(max_length=50,verbose_name="Categoria del equipo")
    responsable = models.ForeignKey(User,on_delete=models.CASCADE)
    imagen = models.ImageField(verbose_name="Foto del artículo",null=True,blank=True,upload_to="img")
    competicion = models.ManyToManyField(Competicion,verbose_name='Competicion')
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    modificado = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

    # Funcion que devuelve los valores escogidos de la clase Moto
    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ["-creado"]

#########################################################################################################################################       

class Jugador(models.Model):
    # crear los campors del modelo, un campo corresponde con una columna de la tabla "principal_piso"
    nombre = models.CharField(max_length=50,unique=True,verbose_name="Nombre del jugador")
    correo = models.EmailField(max_length=50,unique=True,verbose_name="Correo")
    edad = models.IntegerField(verbose_name="Edad")
    imagen = models.ImageField(verbose_name="Foto del jugador",null=True,blank=True,upload_to="fotos")
    equipo = models.ForeignKey(Equipo,on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    modificado = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

    # Funcion que devuelve los valores escogidos de la clase Moto
    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ["-creado"]

#########################################################################################################################################

