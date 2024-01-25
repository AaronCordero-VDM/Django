from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .views import Registro

urlpatterns = [
    path('registro', Registro.as_view(),name='registro'),
]