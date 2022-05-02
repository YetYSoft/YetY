from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from piscinas.forms import Piscina_grande_Form
from piscinas.models import Valores_Piscina


# Create your views here.


# grid inicial piscinas
@login_required
def piscinas_start(request):
       return render(request,"start_piscinas.html")
       
# Formulario de registro valores piscina grande
@login_required
def piscina_grande_registro(request):
    if request.method == "POST":
        form = Piscina_grande_Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('piscinas/piscinas')
    else:
        form=Piscina_grande_Form()
    return render (request,'grid_piscinas.html',{'form':form})