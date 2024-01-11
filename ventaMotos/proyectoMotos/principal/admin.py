from django.contrib import admin
from .models import Moto

# Register your models here.
class MotoAdmin(admin.ModelAdmin):
    list_display = ("precio","marca","modelo","localidad","fechaFabricacion","kilometros")
    # Filtrado
    list_filter = ("marca","localidad")
    # Busquedas
    search_fields = ("marca","modelo","localidad",)

admin.site.register(Moto,MotoAdmin)