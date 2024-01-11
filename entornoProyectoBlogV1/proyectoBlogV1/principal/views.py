from django.shortcuts import render
from .models import Articulo
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def listadoArticulos(request):
    listado = loader.get_template('principal\listado.html')
    articulos = Articulo.objects.all()
    contexto = {
        "articulos":articulos,
    }
    return HttpResponse(listado.render(contexto,request))