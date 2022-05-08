from dataclasses import fields
from django import forms
from django.forms import ModelForm,Textarea, fields_for_model
from django.urls import reverse
#from betterforms.multiform import MultiModelForm # clase para varios modelos en un formulario

from .models import Valores_Piscina


class Form_Piscina_grande(forms.ModelForm):
    class Meta:
        model=Valores_Piscina #nombre del modelo
        template_name = 'piscina_grande_form.html'
       # fields= ( '__all__' ) #campos del modelo
        fields=[
            'Ph',
            'cloro_libre',
            'cloro_total',
            'transparencia',
            'turbidez',
            'presion_filtro',
            'presion_filtro_limpiado',
            'nivel_cloro',
            'nivel_ph',
            'Incidencias',
            'intervencion_realizada',
            'rellenado_cloro',
            'rellenado_Ph'
        ]
     






    widgets = {
        'Ph': forms.NumberInput(attrs={'placeholder': 'Ph      (Entre 6,8 y 7,2)'}),
        'cloro_libre':  forms.NumberInput (attrs={'placeholder': 'Cloro      (Entre 1,5 y 2,0)'}),
        'cloro_total':  forms.NumberInput (attrs={'placeholder': 'Libre (Max 0,6 mayor que cloro)'}),
        'transparencia':forms.NumberInput (attrs={'placeholder': 'Transparencia   (Bien 1 si no 0)'}),
        'turbidez':     forms.NumberInput (attrs={'placeholder': 'Turbidez   (Entre 0 y 5)'}),
        'presion_filtro':forms.NumberInput (attrs={'placeholder': 'Presion filtro (Menor que 1)'}),
        'presion_filtro_limpiado':forms.NumberInput (attrs={'placeholder': 'Filtro limpio    (Menor que 1)'}),
        'nivel_cloro':forms.NumberInput (attrs={'placeholder': 'Nivel Cloro    (mayor del 75%)'}),
        'nivel_ph':forms.NumberInput (attrs={'placeholder': 'Nivel Ph (mayor del 75%)'}),
        'Incidencias':forms.TextInput(attrs={'placeholder': 'Que está pasando?'}),
        'intervencion_realizada':forms.TextInput(attrs={'placeholder': 'Que se ha hecho?'}),
        'rellenado_cloro':forms.CheckboxInput ( attrs={'placeholder': 'Marcar si se ha rellenado ahora'}),

    }  
    
    
'''
         labels=[
            'Ph':,
            'cloro_libre':,
            'cloro_total':,
            'transparencia',
            'turbidez',
            'presion_filtro',
            'presion_filtro_limpiado',
            'nivel_cloro',
            'nivel_ph',
            'Incidencias',
            'intervencion_realizada',
            'rellenado_cloro',
            'rellenado_Ph'
        ]
        
'''
