from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class Articulo(models.Model):
    # crear los campors del modelo, un campo corresponde con una columna de la tabla "principal_piso"
    titulo = models.CharField(max_length=50,unique=True,verbose_name="Titulo del articulo")
    texto = models.TextField(verbose_name="Contenido del articulo")
    imagen = models.ImageField(verbose_name="Foto del articulo",null=True,blank=True,upload_to="fotos")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    modificado = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

    # Funcion que devuelve los valores escogidos de la clase Moto
    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ["-creado"]

class Comentario(models.Model):
    texto = models.TextField(verbose_name="Comentario del articulo")
    articulo = models.ForeignKey(Articulo,on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de comentario")
    modificado = models.DateTimeField(auto_now=True, verbose_name="Fecha de comentario")

    def __str__(self):
        return self.texto[:10]+"..."
    class Meta:
        ordering = ["-creado"]