from django import forms
from django.forms import ModelForm,Textarea
from django.urls import reverse
#from betterforms.multiform import MultiModelForm # clase para varios modelos en un formulario

from piscinas.models import Valores_Piscina


class Piscina_grande_Form(forms.ModelForm):
    class Meta:
        model=Valores_Piscina
        fields= '__all__'
        template_name = 'grid_imputs_piscinas.html'
        