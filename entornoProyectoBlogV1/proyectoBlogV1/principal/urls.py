from django.urls import path
from . import views


urlpatterns = [
    path('articulos/', views.listadoArticulos, name='listado'),
]
