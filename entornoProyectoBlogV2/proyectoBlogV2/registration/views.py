from django.forms.models import BaseModelForm
from django.shortcuts import render
from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django import forms

# Create your views here.

class Registro(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registro.html'

    def get_success_url(self) -> str:
        return reverse_lazy('login') + "?registroOk"
    
    def get_form(self, form_class:None):
        form = super(Registro, self).get_form()

        #Modificar campos
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Nombre de usuario'})
        form.fields['password1'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Contraseña de confirmacion'})

        for fieldname in ['username','password1','password2']:
            forms.fields[fieldname].label = ""
            
        return form