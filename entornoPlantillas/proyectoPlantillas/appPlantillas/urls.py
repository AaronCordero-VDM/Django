from . import views
from django.urls import path

urlpatterns = [
    path('',views.verPlantilla, name="inicial"),
    path('estructura/',views.estructura, name="estructura"),
]