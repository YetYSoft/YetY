from multiprocessing import context
from operator import countOf
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.forms import ModelForm

from espacios.models import *
from espacios.forms import *
from espacios.urls import *
from partes.models import Ot_Ubicaciones

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
def zona_nueva (request):
    data ={ 'form' :zona_nueva_form()  }
    if request.method == "POST":
        form=zona_nueva_form (data=request.POST)
        if form.is_valid():
           form.save()
           return redirect ('zonas_list')
         #  print('//////////////////////////')
         #  print(form)
        else:
            data['form' ] =form
            print('++++++++++++++++++++')
            print(form)
    return render (request, 'zona.html', data)



class zonas_list (ListView): # Lista de departamentos
    model = Zonas
    fields= '__all__'
    template_name = 'zonas_list.html'
    ordering = ['nombre']
    paginate_by = 25
    context_object_name = 'list' # Esto es lo que envía al template

def zonas_edit(request,pk):
    zonas = Zonas.objects.get(id=pk)
    if request.method == "GET":
        form = zona_edit_form(instance=zonas)
        print("--------------------------")
       # print(form)
    else:
        form=zona_edit_form(request.POST,instance=zonas)
        print("Es valido? ++++++++++++++++++++++++++++++++")
       
        if form.is_valid():
            print("Es valido ++++++++++++++++++++++++++++++++")
            form.save()
            print("Guardado ++++++++++++++++++++++++++++++++")
        return redirect('zonas_edit', pk )
    print("////////////////////////////")
    print (type(pk))
    return render (request,'zona.html',{'form':form, 'url':'zonas_edit', "pk":pk })



class Zonas_listado (ListView): # Lista de departamentos
    model = Zonas
    fields= '__all__'
    template_name = 'zonas_listado.html'
    ordering = ['nombre']
    paginate_by = 25
    context_object_name = 'list' # Esto es lo que envía al template





####################   Ubicaciones   ###########################


def ubicacion_nueva (request):
    data ={ 'form' :ubicacion_nueva_form()  }
    if request.method == "POST":
        form=ubicacion_nueva_form (data=request.POST)
        if form.is_valid():
           form.save()
           return redirect ('ubicacion_list')
         #  print('//////////////////////////')
         #  print(form)
        else:
            data['form' ] =form
            print('++++++++++++++++++++')
            print(form)
    return render (request, 'ubicacion.html', data)



class ubicacion_list (ListView): # Lista de departamentos
    model = Ubicaciones
    fields= '__all__'
    template_name = 'ubicacion_list.html'
    ordering = ['nombre']
    paginate_by = 25
    context_object_name = 'list' # Esto es lo que envía al template


def ubicacion_edit(request,pk):
    ubicacion = Ubicaciones.objects.get(id=pk)

    print("_________________________")
    #total_ubicaciones=len(Ubicaciones.objects.all)
    #print(total_ubicaciones)
    print("__________________________")

    if request.method == "GET":
        form = ubicacion_edit_form(instance=ubicacion)
        print("--------------------------")
       # print(form)
    else:
        form=ubicacion_edit_form(request.POST,instance=ubicacion)
       
        if form.is_valid():
            
            form.save()
        return redirect('ubicacion_edit',pk)
    return render (request,'ubicacion.html',{'form':form, 'url':'ubicacion_edit', "pk":pk })



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
    ubicacion = Puertas.objects.get(id=pk)
    if request.method == "GET":
        form = Puerta_edit_form(instance=ubicacion)
        print("--------------------------")
       # print(form)
    else:
        form=Puerta_edit_form(request.POST,instance=ubicacion)
       
        if form.is_valid():
            print("////////////////////////////")

            form.save()
        return redirect('puerta_edit',pk)
    return render (request,'puerta.html',{'form':form, 'url':'puerta_edit', "pk":pk})



############     Llaves   ###################

def llave_nueva (request):
    data ={ 'form' :llave_nueva_form()  }
    if request.method == "POST":
        form=llave_nueva_form (data=request.POST)
        if form.is_valid():
           form.save()
           return redirect ('llave_list')
         #  print('//////////////////////////')
         #  print(form)
        else:
            data['form' ] =form
            print('++++++++++++++++++++')
            print(form)
    return render (request, 'llave.html', data)



class llave_list (ListView): # Lista de departamentos
    model = llaves
    fields= '__all__'
    template_name = 'llave_list.html'
    ordering = ['nombre']
    paginate_by = 25
    context_object_name = 'list' # Esto es lo que envía al template


def llave_edit(request,pk):
    ubicacion = llaves.objects.get(id=pk)
    if request.method == "GET":
        form = llave_edit_form(instance=ubicacion)
        print("--------------------------")
       # print(form)
    else:
        form=llave_edit_form(request.POST,instance=ubicacion)
       
        if form.is_valid():
            print("////////////////////////////")

            form.save()
        return redirect('llave_edit',pk)
    return render (request,'llave.html',{'form':form, 'url':'llave_edit', "pk":pk})







#######  Zona User   ############

# listado de Habs o Ubicaciones 
class Zonas_user_list (ListView) :
    model = Zonas
    fields= '__all__'
    template_name = 'zona_user_list.html'
    ordering = ['nombre']
    paginate_by = 25
    context_object_name = 'list' # Esto es lo que envía al template 




class Zonas_user (ListView) :
    pass

class ubicacion_user_list (ListView): # Lista de departamentos
    model = Ubicaciones
    fields= '__all__'
    template_name = 'ubicacion_user_list.html'
    ordering = ['nombre']
    paginate_by = 20
    context_object_name = 'list' # Esto es lo que envía al template 
    def get_queryset(self):
        return Ubicaciones.objects.filter(zona=self.kwargs['pk'])

class ubicacion_user (ListView): # Lista de departamentos
    pass


#####################   select #################

def zona_select (request):
    zona=Zonas.objects.all().order_by('nombre')
    form=zona
    return render (request,'zona_select.html',{'form':form })

def ubicaciones_select (request):
    variable= request.GET.get('select_zona')  #####  este select viene de <select name="select_zona" class="form-control" hx-get="/espacios/ubicaciones_select/"
    ubicaciones=Ubicaciones.objects.filter(zona=variable).order_by('nombre')
    list=ubicaciones
    return render (request,'ubicaciones_select.html',{'list':list })

def ubicacion_menu (request, pk):
    ubicacion = Ubicaciones.objects.get(id=pk)
    return render (request,'ubicacion_menu.html', {'ubicacion':ubicacion} )



###############   Busqueda Habitaciones     ##############################   

def habitaciones_buscar (request):
    return render (request,'habitaciones_buscar.html',{'list':list })

def habitaciones_encontrar (request):
    print ("____________________________")

    buscado= request.POST.get("search")  #####  este select viene de <select name="select_zona" class="form-control" hx-get="/espacios/ubicaciones_select/"
    habitaciones=Ubicaciones.objects.filter(zona=3).filter(nombre__istartswith=buscado).order_by('nombre')
    list=habitaciones
    print ("____________________________")
    print (request)
    print (buscado)

    print ("____________________________")
    return render (request,'habitaciones_grid.html',{'list':list })



#.filter(nombre=buscado)











def pruebas (request):
    ubic=Ubicaciones.objects.filter(nombre__istartswith=12).values('nombre',"id")[:5]
    ubica=ubic
    for i in ubica:
        print('_________________-')
        print ("tipo variable" ,type(ubic))
        print ("valor",ubic)
        print ("tipo variable" ,type(ubica))
        print ("valor",ubica)
        print('_________________-')
    return render (request,'pruebas.html')