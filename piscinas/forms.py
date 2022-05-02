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
            'cloro_libre': forms.NumberInput(attrs={'placeholder': 'Cloro      (Entre 1,0 y 1,5)'}),
        }