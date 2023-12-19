from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Create your views here.
def listadoPersonas(request):
    personas = [
        {"nombre": "Carlos", "edad": 34, "ciudad": "Madrid", "profesion": "Ingeniero"},
        {"nombre": "Luisa", "edad": 28, "ciudad": "Buenos Aires", "profesion": "Diseñadora"},
        {"nombre": "Amina", "edad": 42, "ciudad": "El Cairo", "profesion": "Médica"},
        {"nombre": "Sergei", "edad": 30, "ciudad": "Moscú", "profesion": "Programador"},
        {"nombre": "Yumi", "edad": 25, "ciudad": "Tokio", "profesion": "Chef"}
    ]
    plantilla = loader.get_template('listadoEnTabla.html')
    contexto = {
        'listaPersonas':personas
    }
    return HttpResponse(plantilla.render(contexto, request));