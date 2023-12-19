from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Piso, Cliente

# Create your views here.
def catalogo(request):
    # Cargamos el template a usar en la funcion
    catalogo = loader.get_template('principal\catalogo.html')

    contexto = {
    # Llamada a la base de datos para pedir todos los pisos
        'pisos':Piso.objects.all(),
        'clientes':Cliente.objects.all(),
    }

    return HttpResponse(catalogo.render(contexto,request))

def crearCliente(request):
    cli = Cliente(nombre="Pepe",apellidos="Fernandez Fernande",telefono="623727237",correo="pepe@gmail.com",inversor=False)
    cli.save()
    return HttpResponseRedirect(reverse('catalogo'))

def modificarCliente(request):
    cli = Cliente.objects.get(id=1)
    cli.telefono = "623423494"
    cli.save()
    return HttpResponseRedirect(reverse('catalogo'))

def borrarCliente(request):
    cli = Cliente.objects.last()
    cli.delete()
    return HttpResponseRedirect(reverse('catalogo'))