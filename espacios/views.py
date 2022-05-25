from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.forms import ModelForm

from espacios.models import *
from espacios.forms import *
from espacios.urls import *

from django.forms import ValidationError 
# Create your views here.






class Departamentos_list (ListView): # Lista de departamentos
    model = Departamentos
    fields= ['nombre']
    template_name = 'Departamentos_list.html'
    ordering = ['nombre']
    paginate_by = 25
    context_object_name = 'list' # Esto es lo que envía al template


def nuevo_departamento (request):
    data ={ 'form' :Nuevo_departamento_form()  }

    if request.method == "POST":
        form=Nuevo_departamento_form (data=request.POST)
        if form.is_valid():
           form.save()
            
        else:
            data['form' ] =form


     
    return render (request, 'departamento_form.html', data)

  
