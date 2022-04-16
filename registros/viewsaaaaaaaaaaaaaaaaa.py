from __future__ import print_function
from cgi import print_arguments
from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from registros.models import Ot_Temp_Clima_Interior, Ot_Temp_Minibar,Ot_Pedido_material
from registros.forms import Temp_Clima_Form, Pedido_Form
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Registro temperaturas...........................................

# listados
class Temp_Clima (ListView):
    model = Ot_Temp_Clima_Interior
    paginate_by = 100
    ordering = ['field','-fecha_hora_cambio_ot']
    template_name = 'registros/ot_registro_temp_lista.html'
    print (User.user_permissions)
    print("juan")


# Editar registros de Clima
@login_required
def Temp_Clima_nuevo(request):
    if request.method == "POST":
        form = Temp_Clima_Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ListaTempHabs')
    else:
        form=Temp_Clima_Form()
    return render (request,'registros/ot_registro_edit_form.html',{'form':form})

@login_required
def Temp_Clima_editar(request,num_Temp_Clima):
    registro = Ot_Temp_Clima_Interior.objects.get(num_Temp_Clima=num_Temp_Clima)
    if request.method == "GET":
        form = Temp_Clima_Form(instance=registro)
    else:
        form=Temp_Clima_Form(request.POST,instance=registro)
        if form.is_valid():
            form.save()
        return redirect('ListaTempHabs')
    return render (request,'registros/ot_registro_edit_form.html',{'form':form})


# Pedidos...........................................

# listados
class Pedidos_list (ListView):
    model = Ot_Pedido_material
    paginate_by = 100
    ordering = ['estado_ot','-fecha_hora_cambio_ot']
    template_name = 'registros/ot_pedidos_lista.html'
    print(get_user_permissions()
  


# Editar registros de PEDIDOS ................
@login_required
def Pedido_nuevo(request):
    if request.method == "POST":
        form = Pedido_Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ListaPedidos')
    else:
        form=Pedido_Form()
    
    return render (request,'registros/ot_Pedidos_edit_form.html',{'form':form})

@login_required
def Pedido_editar(request,num_Pedido):
    pedido = Ot_Pedido_material.objects.get(num_Pedido=num_Pedido)
    if request.method == "GET":
        form = Pedido_Form(instance=pedido)
    else:
        form=Pedido_Form(request.POST,instance=pedido)
        if form.is_valid():
            form.save()
        return redirect('ListaPedidos')
    return render (request,'registros/ot_Pedidos_edit_form.html',{'form':form})
