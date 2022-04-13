from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def iniciorondas(request):
    return render (request,'ot_parte_list_elemento.html', listado)
    #return render (request,'sidebar.html')
    return HttpResponse ('Menu de Rondas')
