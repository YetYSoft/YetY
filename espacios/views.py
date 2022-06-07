from multiprocessing import context
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.forms import ModelForm
from requests import request

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
        form = Planta_o_zona_edit_form(instance=zonas)
        print("--------------------------")
       # print(form)
    else:
        form=Planta_o_zona_edit_form(request.POST,instance=zonas)
        print("Es valido? ++++++++++++++++++++++++++++++++")
       
        if form.is_valid():
            print("Es valido ++++++++++++++++++++++++++++++++")
            form.save()
            print("Guardado ++++++++++++++++++++++++++++++++")
            
        return redirect('/espacios/Plantas_o_zonas_list/')
    print("////////////////////////////")
    print (type(pk))
    return render (request,'Planta_o_zona.html',{'form':form,"pk":pk })



class Zonas_listado (ListView): # Lista de departamentos
    model = Planta_o_zonas
    fields= '__all__'
    template_name = 'zonas_listado.html'
    ordering = ['nombre']
    paginate_by = 25
    context_object_name = 'list' # Esto es lo que envía al template





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
        form = Hab_cuarto_sala_edit_form(instance=cuarto)
        print("--------------------------")
       # print(form)
    else:
        form=Hab_cuarto_sala_edit_form(request.POST,instance=cuarto)
       
        if form.is_valid():
            print("////////////////////////////")

            form.save()
        return redirect('/espacios/Hab_cuarto_sala_list/')
    return render (request,'Hab_cuarto_sala.html',{'form':form})



############     Puertas   ###################

def puerta_nueva (request):
    data ={ 'form' :Puerta_nueva_form()  }
    if request.method == "POST":
        form=Puerta_nueva_form (data=request.POST)
        if form.is_valid():
           form.save()
           return redirect ('puerta_list')
         #  print('//////////////////////////')
         #  print(form)
        else:
            data['form' ] =form
            print('++++++++++++++++++++')
            print(form)
    return render (request, 'puerta.html', data)



class puerta_list (ListView): # Lista de departamentos
    model = Puertas
    fields= '__all__'
    template_name = 'puerta_list.html'
    ordering = ['nombre']
    paginate_by = 25
    context_object_name = 'list' # Esto es lo que envía al template


def puerta_edit(request,pk):
    cuarto = Puertas.objects.get(id=pk)
    if request.method == "GET":
        form = Puerta_edit_form(instance=cuarto)
        print("--------------------------")
       # print(form)
    else:
        form=Puerta_edit_form(request.POST,instance=cuarto)
       
        if form.is_valid():
            print("////////////////////////////")

            form.save()
        return redirect('/espacios/puerta_list/')
    return render (request,'puerta.html',{'form':form})






















#######  Zona User   ############

# listado de Habs o Ubicaciones 

class Habs_listado (ListView): # Lista de departamentos
    model = Habs_cuartos_salas
    fields= '__all__'
    template_name = 'Habs_listado.html'
    ordering = ['nombre']
    paginate_by = 25
    context_object_name = 'list' # Esto es lo que envía al template 
    def get_queryset(self):
        return Habs_cuartos_salas.objects.filter(planta_o_zona=self.kwargs['pk'])
    #queryset =Habs_cuartos_salas.objects.filter(planta_o_zona = self.kwargs['pk'])




class Hab_user (ListView) :
    pass