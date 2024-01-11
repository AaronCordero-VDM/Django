from django.contrib import admin
from .models import Articulo, Comentario

# Register your models here.
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ("id","titulo","texto","imagen","creado","modificado")

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("id","texto","articulo","creado","modificado")


admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Comentario, ComentarioAdmin)