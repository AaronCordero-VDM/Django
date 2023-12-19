from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse
# Create your models here.

def verPlantilla(request):
    plantilla = loader.get_template("appPlantillas\plantilla.html")
    contexto = {
        'escribe':True,
        'presenta':'letras',
        'listaNumeros':[1,3,4,6,3],
        'listaLetras':["A","B","C","D"],
    }
    return HttpResponse(plantilla.render(contexto, request))

def estructura(request):
    plantilla = loader.get_template("appPlantillas\estructura.html")
    contexto = {
        'listaLetras':["A","B","C","D"],
    }
    return HttpResponse(plantilla.render(contexto, request))