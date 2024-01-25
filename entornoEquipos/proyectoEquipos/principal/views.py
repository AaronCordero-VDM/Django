from django.shortcuts import render
from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Equipo, Competicion, Jugador
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

class inicio(TemplateView):
    template_name = 'principal/inicio.html'

class listadoEquipos(ListView):
    model = Equipo

class listadoCompeticiones(ListView):
    model = Competicion

class listadoJugadores(ListView):
    model = Jugador


@method_decorator(login_required,name='dispatch')
class crearEquipo(CreateView):
    model = Equipo
    fields = ["nombre", "categoria", "imagen", "competicion"]
    success_url = reverse_lazy('listadoEquipos')

    def form_valid(self, form):
        form.instance.responsable = self.request.user
        return super(crearEquipo, self).form_valid(form)

@method_decorator(login_required,name='dispatch')
class crearJugador(CreateView):
    model = Jugador
    fields = ["nombre","correo","edad","imagen","equipo"]
    success_url = reverse_lazy('listadoJugadores')

    def form_valid(self, form):
        form.instance.responsable = self.request.user
        return super(crearJugador, self).form_valid(form)
    
@method_decorator(login_required,name='dispatch')
class crearCompeticion(CreateView):
    model = Competicion
    fields = ["nombre","lugar"]
    success_url = reverse_lazy('listadoCompeticiones')

    def form_valid(self, form):
        form.instance.responsable = self.request.user
        return super(crearCompeticion, self).form_valid(form)

@method_decorator(login_required,name='dispatch')
class borrarEquipo(DeleteView):
    model = Equipo
    success_url = reverse_lazy('listadoEquipo')
    
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        equipo = self.get_object() # Me devuelve el articulo que sequiere modficar
        if (equipo.responsable != request.user):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    
@method_decorator(login_required,name='dispatch')
class modificarEquipo(UpdateView):
    model = Equipo
    fields = ["texto", "imagen", "categorias"]
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('listado')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        equipo = self.get_object() # Me devuelve el articulo que sequiere modficar
        if (equipo.responsable != request.user):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)