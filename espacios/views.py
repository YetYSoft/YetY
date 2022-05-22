from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from espacios.models import *
from espacios.forms import *
from espacios.urls import *

from django.forms import ValidationError 
# Create your views here.



class nuevo_departamento_form(CreateView):
    def clean_nombre(self):
        nombre= self.cleaned_data ['nombre']
        existe = nombre.objects.filter (nombre__iexact=nombre).exists()
        if existe:
            raise ValidationError("Ya existe este departamento")
        return nombre

    model = Departamentos
    fields= ['nombre']
    template_name = 'departamento_form.html'
    success_url= '/espacios/Departamentos_list'
    widgets={
            'departamento':forms.TextInput(attrs={'class':'form-control','placeholder': 'Nombre departamento', }),
        }


class Departamentos_list (ListView): # Lista de departamentos
    model = Departamentos
    fields= ['nombre']
    template_name = 'Departamentos_list.html'
    ordering = ['nombre']
    paginate_by = 25
    context_object_name = 'list' # Esto es lo que envía al template




  
