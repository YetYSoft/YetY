from multiprocessing import context
from django.shortcuts import render,redirect
from django.shortcuts import get_list_or_404, get_object_or_404

from django.http import HttpResponse

from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
from django.urls import reverse

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User



from partes.forms import ParteForm, Nuevo_form, TrabajosForm, TrabajosEditForm, Elemento_list_form
from partes.models import Ot_Parte, Ot_Ubicaciones, Ot_Elementos, Ot_Trabajos, Ot_Etiquetas, Ot_Pedidos

from django.forms.models import modelformset_factory # model form para querysets 
 




########### combinar dos modelos en un template




    
# ......Ejemplo escribir registros en base de datos
#           variable=modelo(campo1=valor_en_campo1,campo2=valor_en_campo2, etc)  
#         y esto escribe los valores en la base de datos
#           variable.save()   

#.........lo mismo Abreviado      
#           variable=modelo.objets.create(campo1=valor_en_campo1,campo2=valor_en_campo2, etc)  

# ......Ejemplo modificar registros en base de datos
#           variable=modelo(campo1=valor_en_campo1,campo2=valor_en_campo2, etc)  
#           variable.save()   

#           variable=modelo.objets.get(campo1=valor_en_campo1,
#           variable.delete()   
#           
#........recupera el modelo completo
#           variable=modelo.objets.all()


def busqueda(request):
     return render(request,'prueba.html')

def buscar(request):

    if request.GET["prd"]: # comprueba que el formulario no esté vacío
        palabra_recibida=request.GET["prd"]
        partes=Ot_Parte.objects.filter(descripcion_ot__icontains=palabra_recibida) [:10]
        print(type(partes))
        print(partes.query)
        return render(request,"prueba_resultados.html",{"los_partes":partes,"palabra_recibida":palabra_recibida})
    else:
        
        return HttpResponse("no has puesto nada")

            
 # def parte_y_trabajos(request,num_parte):
  #   los_partes =Ot_Parte.objects.filter(ubicacion_ot=ubicaci).order_by('estado_ot','-fecha_cambio_ot','-fecha_hora_cambio_ot','elemento_ot')
   #   listado = {'los_partes':los_partes}
    #  return render (request,'ot_parte_list_ubicacion.html', listado)











#------------------Parte-----------------
@login_required
def index(request):
    return redirect('Partes_Pendientes')
    #return render (request,'sidebar.html')


class DetalleParte(DetailView):
    model = Ot_Parte
    template_name = 'ot_parte_detail.html'
    





 
#--------------Formularios para listados parte---------
@login_required
def ubicacion_list_form(request):
    form = Nuevo_form()
    return render (request,'ot_ubicaciones_lista_form.html',{'form':form})

@login_required
def elemento_list_form(request):#-
    form = Elemento_list_form()
    return render (request,'ot_elementos_lista_form.html',{'form':form})

@login_required
def ubicacion_lista_partes(request): # Recoje el dato del form
    if 'ubicacion_ot' in request.GET:
        ubicaci=request.GET['ubicacion_ot']
        return redirect('PartesPorUbicacion',ubicaci) #  Envia el daro al template del listado
@login_required
def elemento_lista_partes(request): # Recoje el dato del form
    if 'elemento_ot' in request.GET:
        element=request.GET['elemento_ot']
        return redirect('PartesPorElemento',element) #  Envia el daro al template del listado













#------------------Listados Parte---------------------
@login_required
def PartesPorUbicacion (request, ubicaci):
    los_partes =Ot_Parte.objects.filter(ubicacion_ot=ubicaci).order_by('estado_ot','-fecha_cambio_ot','-fecha_hora_cambio_ot','elemento_ot')
    listado = {'los_partes':los_partes}
    return render (request,'ot_parte_list_ubicacion.html', listado)

@login_required
def PartesPorElemento (request, element):
    los_partes =Ot_Parte.objects.filter(elemento_ot=element).order_by('estado_ot','-fecha_cambio_ot','-fecha_hora_cambio_ot','ubicacion_ot')
    listado = {'los_partes':los_partes}
    return render (request,'ot_parte_list_elemento.html', listado)


class partes_pendientes (ListView):#Urgentes arriba, seguidos de los mas nuevos
    model = Ot_Parte
    paginate_by = 50
    ordering = ['prioridad_ot','-fecha_cambio_ot','-fecha_hora_cambio_ot','-num_ot']
    queryset =Ot_Parte.objects.exclude(estado_ot = "Terminado")
    template_name = 'ot_parte_lista_pendientes.html'

class partes (ListView): #Ultimos partes nuevos o modificados, terminados o no
    model = Ot_Parte
    template_name = 'ot_parte_lista.html'
    ordering = ['-fecha_cambio_ot','-fecha_hora_cambio_ot','-num_ot']
    paginate_by = 25




#-------Formulario de PARTE NUEVO Existe?---------
@login_required
def nuevo_form(request):
    form = Nuevo_form()
    return render (request,'ot_ubicaciones_nuevo_lista_form.html',{'form':form})

@login_required
def nuevo_lista_partes(request): # Recoje el dato del form
    if 'ubicacion_ot' in request.GET:
        ubicaci=request.GET['ubicacion_ot']
        return redirect('PartesPorUbicacion',ubicaci) #  Envia el daro al template del listado




#-------Formulario de PARTE NUEVO/EDITAR ---------
@login_required
def parte_nuevo(request):
    if request.method == "POST":
        form = ParteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Listapartes')
    else:
        form=ParteForm()
    return render (request,'ot_parte_edit_form.html',{'form':form})

@login_required
def parte_editar(request,num_ot):
    parte = Ot_Parte.objects.get(num_ot=num_ot)
    if request.method == "GET":
        form = ParteForm(instance=parte)
    else:
        form=ParteForm(request.POST,instance=parte)
        if form.is_valid():
            form.save()
        return redirect('Partes_Pendientes')
    return render (request,'ot_parte_edit_form.html',{'form':form})






#---------------Trabajos--------------------------



class ListaTrab(ListView):#Ultimos trabajos realizados
    model = Ot_Trabajos
    paginate_by = 25
    ordering = ['-fecha_cambio_tra','-num_tra']
    template_name = 'ot_trabajos_list.html'

class ListaTrabParte(ListView): #listado por numero de parte
    model = Ot_Trabajos
    paginate_by = 10
    ordering = ['-fecha_cambio_tra','-fecha_hora_cambio_tra','-num_tra']
    template_name = 'ot_trabajos_list_por_parte.html'
    def get_queryset(self):
        return Ot_Trabajos.objects.filter(num_ot_tra=self.kwargs['numero_ot'])

@login_required
def NuevoTrab (request,numero_ot):
    parte = Ot_Parte.objects.get(num_ot=numero_ot)

    if request.method == "POST":

        form = TrabajosForm(request.POST)

        if form.is_valid():
            form.save()
        #return redirect('lista_trabajo')
        return redirect('ver_trabajos',numero_ot)
    else:
        form=TrabajosForm(initial={'num_ot_tra': numero_ot})

    return render (request,'ot_trabajos_nuevo_form.html',{'form':form,'numero_ot':numero_ot, 'parte':parte})

@login_required
def EditarTrab (request,num_tra,numero_ot):
    trabajo = Ot_Trabajos.objects.get(num_tra=num_tra)
    parte = Ot_Parte.objects.get(num_ot=numero_ot)
    if request.method == "GET":
        form = TrabajosEditForm(instance=trabajo)
    else:
        form=TrabajosEditForm(request.POST,instance=trabajo)
        if form.is_valid():
            form.save()
        return redirect('ver_trabajos',numero_ot)
    #return render (request,'ot_trabajos_edit_form.html',{'form':form,'numero_ot':numero_ot, 'parte':parte,'form.num_ot_tra.value':911})
    return render (request,'ot_trabajos_edit_form.html',{'form':form, 'parte':parte})


#@login_required
#def ListaTrab_parte(request, numparte):

 #       los_trabajos =Ot_Trabajos.objects.filter(num_ot_tra=numparte).order_by('-fecha_cambio_ot','num_ot_tra','estado_ot')
 #       listado = {'los_trabajos':los_trabajos}
 #       return render (request,'ot_trabajos_list', listado)
        
    


