from django.urls import path
from .views import inicio, listadoEquipos, crearEquipo, listadoCompeticiones, crearJugador, listadoJugadores, crearCompeticion, borrarEquipo, modificarEquipo

urlpatterns = [
    path('', inicio.as_view(), name='inicio'),
    path('listadoEquipos', listadoEquipos.as_view(), name='listadoEquipos'),
    path('listadoCompeticiones', listadoCompeticiones.as_view(), name='listadoCompeticiones'),
    path('listadoJugadores', listadoJugadores.as_view(), name='listadoJugadores'),
    path('crearEquipo', crearEquipo.as_view(), name='crearEquipo'),
    path('crearJugador', crearJugador.as_view(), name='crearJugador'),
    path('crearCompeticion', crearCompeticion.as_view(), name='crearCompeticion'),
    path('borrarEquipo/<int:pk>', borrarEquipo.as_view(), name='borrarEquipo'),
    path('modificarEquipo/<int:pk>', modificarEquipo.as_view(), name='modificarEquipo'),
]
