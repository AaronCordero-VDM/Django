from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Moto

# Create your views here.
def catalogo(request):
    # Cargamos el template a usar en la funcion
    catalogo = loader.get_template('principal\catalogo.html')

    contexto = {
    # Llamada a la base de datos para pedir todos los pisos
        'motos':Moto.objects.all(),
    }

    return HttpResponse(catalogo.render(contexto,request))
