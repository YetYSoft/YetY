from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from piscinas.forms import Form_Piscina_grande
from piscinas.models import Valores_Piscina


# Create your views here.


# grid inicial piscinas
@login_required
def piscinas_start(request):
       return render(request,"start_piscinas.html")


# Formulario de registro valores piscina grande
@login_required
def piscina_grande(request):
    if request.method == "POST":
        form = Form_Piscina_grande(request.POST)
        if form.is_valid():
            form.save()
        return redirect('piscinas/piscinas')
    else:
       form = Form_Piscina_grande(request.POST)
    return render (request,"piscina_grande_form.html", {"form": form}) 