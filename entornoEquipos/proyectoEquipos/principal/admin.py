from django.contrib import admin

# Register your models here.

from .models import Equipo, Jugador, Competicion

class EquipoAdmin(admin.ModelAdmin):
    list_display = ("id","nombre","categoria","creado","modificado")

admin.site.register(Equipo, EquipoAdmin)

class CompeticionAdmin(admin.ModelAdmin):
    list_display = ("nombre","lugar","creado","modificado")

admin.site.register(Competicion, CompeticionAdmin)

class JugadorAdmin(admin.ModelAdmin):
    list_display = ("nombre","correo","edad","imagen","equipo","creado","modificado")

admin.site.register(Jugador, JugadorAdmin)