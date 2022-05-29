from django.shortcuts import redirect, render
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



#####################       Departamentos    #########################
def Departamento_nuevo (request):
    data ={ 'form' :Nuevo_departamento_form()  }
    if request.method == "POST":
        form=Nuevo_departamento_form (data=request.POST)
        if form.is_valid():
           form.save()
           return redirect ('Departamentos_list')
         #  print('//////////////////////////')
         #  print(form)
        else:
            data['form' ] =form
            print('++++++++++++++++++++')
            print(form)

   
    return render (request, 'Departamento.html', data)

class Departamentos_list (ListView): # Lista de departamentos
    model = Departamentos
    fields= ['nombre',id]
    template_name = 'Departamentos_list.html'
    ordering = ['nombre']
    paginate_by = 25
    context_object_name = 'list' # Esto es lo que envía al template



def Departamento_edit(request,pk):
    departamento = Departamentos.objects.get(id=pk)
    if request.method == "GET":
        form = Nuevo_departamento_form(instance=departamento)
        print("--------------------------")
       # print(form)
    else:
        form=Nuevo_departamento_form(request.POST,instance=departamento)
        if form.is_valid():
            print("////////////////////////////")

            form.save()
        return redirect('/espacios/Departamentos_list/')
    return render (request,'Departamento.html',{'form':form})




  ##########################   Plantas_o_zonas   ######################3
def Planta_o_zona_nueva (request):
    data ={ 'form' :Planta_o_zona_nueva_form()  }
    if request.method == "POST":
        form=Planta_o_zona_nueva_form (data=request.POST)
        if form.is_valid():
           form.save()
           return redirect ('Plantas_o_zonas_list')
         #  print('//////////////////////////')
         #  print(form)
        else:
            data['form' ] =form
            print('++++++++++++++++++++')
            print(form)
    return render (request, 'Planta_o_zona.html', data)



class Plantas_o_zonas_list (ListView): # Lista de departamentos
    model = Planta_o_zonas
    fields= '__all__'
    template_name = 'Plantas_o_zonas_list.html'
    ordering = ['nombre']
    paginate_by = 25
    context_object_name = 'list' # Esto es lo que envía al template

def Plantas_o_zonas_edit(request,pk):
    zonas = Planta_o_zonas.objects.get(id=pk)
    if request.method == "GET":
        form = Planta_o_zona_nueva_form(instance=zonas)
        print("--------------------------")
       # print(form)
    else:
        form=Planta_o_zona_nueva_form(request.POST,instance=zonas)
       
        if form.is_valid():

            form.save()
        return redirect('/espacios/Plantas_o_zonas_list/')
    print("////////////////////////////")
    print (type(pk))
    return render (request,'Planta_o_zona.html',{'form':form,"pk":pk })




####################   Hab_cuarto_sala   ###########################


def Hab_cuarto_sala_nueva (request):
    data ={ 'form' :Hab_cuarto_sala_nueva_form()  }
    if request.method == "POST":
        form=Hab_cuarto_sala_nueva_form (data=request.POST)
        if form.is_valid():
           form.save()
           return redirect ('Hab_cuarto_sala_list')
         #  print('//////////////////////////')
         #  print(form)
        else:
            data['form' ] =form
            print('++++++++++++++++++++')
            print(form)
    return render (request, 'Hab_cuarto_sala.html', data)



class Hab_cuarto_sala_list (ListView): # Lista de departamentos
    model = Habs_cuartos_salas
    fields= '__all__'
    template_name = 'Hab_cuarto_sala_list.html'
    ordering = ['nombre']
    paginate_by = 25
    context_object_name = 'list' # Esto es lo que envía al template


def Hab_cuarto_sala_edit(request,pk):
    cuarto = Habs_cuartos_salas.objects.get(id=pk)
    if request.method == "GET":
        form = Hab_cuarto_sala_nueva_form(instance=cuarto)
        print("--------------------------")
       # print(form)
    else:
        form=Hab_cuarto_sala_nueva_form(request.POST,instance=cuarto)
       
        if form.is_valid():
            print("////////////////////////////")

            form.save()
        return redirect('/espacios/Hab_cuarto_sala_list/')
    return render (request,'Hab_cuarto_sala.html',{'form':form})