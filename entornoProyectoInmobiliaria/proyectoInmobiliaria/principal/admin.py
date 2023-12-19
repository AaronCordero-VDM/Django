from django.contrib import admin
from .models import Piso, Cliente

class PisoAdmin(admin.ModelAdmin):
    list_display = ("numReferencia","poblacion","direccion","precio","fechaAlta","fechaModificacion")
    # Filtrado
    list_filter = ("poblacion","cp")
    # Busquedas
    search_fields = ("poblacion",)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre","apellidos","telefono","correo")
    search_fields = ("nombre",)

# Register your models here.
admin.site.register(Piso, PisoAdmin)
admin.site.register(Cliente, ClienteAdmin)