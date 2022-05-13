from django import forms
from django.forms import ModelForm,Textarea
from django.urls import reverse
#from betterforms.multiform import MultiModelForm # clase para varios modelos en un formulario

from partes.models import Ot_Parte,Ot_Trabajos,Ot_Ubicaciones










#--------------Formularios para Editar o nuevo Parte---------
class ParteForm(forms.ModelForm):
    class Meta:
        model=Ot_Parte
        ordering = ["-fecha_cambio_ot"]
        fields= '__all__'
        template_name = 'ot_parte_edit_form.html'
        widgets={
            'ubicacion_ot':forms.Select(),
            'descripcion_ot':forms.Textarea()
        }

#--------------Formularios para Editar o nuevo trabajo---------

class TrabajosForm(forms.ModelForm):
    class Meta:
        model=Ot_Trabajos
        ordering = ["-fecha_cambio_tra"]
        template_name = 'partes/ot_trabajos_nuevo_form.html'

        fields= [
            'num_ot_tra',
            'descripcion_tra'
        ]
        widgets={
            'num_ot_tra':forms.TextInput(attrs={'class':'form-control'} ),
            'descripcion_tra':forms.TextInput(attrs={'class':'form-control'}),
         }
        labels={
             'num_ot_tra':'Numero de parte',
             'descripcion_tra':'Descripcion de trabajo',
          }

class TrabajosEditForm(forms.ModelForm):
    class Meta:
        model=Ot_Trabajos
        template_name = 'partes/ot_trabajos_edit_form.html'
        fields= '__all__'
        widgets={
            'num_ot_tra':forms.TextInput(attrs={'class':'form-control'} ),
            'descripcion_tra':forms.TextInput(attrs={'class':'form-control'}),
         }

#class TrabajoTerminarParteForm(MultiModelForm):
#    form_classes={
#       'Ot_Parte':ParteForm,
#        'Ot_Trabajos':TrabajosForm,
#       }

 




#--------------Formularios para listados parte---------
class Nuevo_form(forms.ModelForm):
    class Meta:
        model = Ot_Parte
        ordering = ["-fecha_cambio_ot"]
        fields =['ubicacion_ot']
        template_name = 'partes/ot_ubicaciones_lista_form.html'
        widgets={
            'ubicacion_ot':forms.Select(attrs={'class':'form-control'} )
            }

class Ubicacion_list_form(forms.ModelForm):
    class Meta:
        model = Ot_Parte
        ordering = ["-fecha_cambio_ot"]
        fields =['ubicacion_ot']
        template_name = 'partes/ot_ubicaciones_lista_form.html'
        widgets={
            'ubicacion_ot':forms.Select(attrs={'class':'form-control'} )
            }

class Elemento_list_form(forms.ModelForm):
    class Meta:
        model = Ot_Parte
        ordering = ["-fecha_cambio_ot"]
        fields =['elemento_ot']
        template_name = 'partes/ot_elementos_lista_form.html'
        widgets={
            'elemento_ot':forms.Select(attrs={'class':'form-control'} )
            }
