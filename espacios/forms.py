from cProfile import label
from django import forms
from django.forms import ModelForm,Textarea, ValidationError

from espacios.models import *
from espacios.urls import *
from django.forms import ValidationError



class Nuevo_departamento_form(forms.ModelForm):
    class Meta:
        model = Departamentos
        fields= ['nombre']
      #  template_name = 'departamento_form.html'
      #  success_url= '/espacios/Departamentos_list'
   #     widgets={
   #             'departamento':forms.TextInput(attrs={'class':'form-control','placeholder': 'Nombre departamento', }),
   #         }

    
    def clean_nombre(self):
        nombre_dep= self.cleaned_data ['nombre']
     #   print ("/////////////////////")
    #    print (nombre)
        existe = Departamentos.objects.filter (nombre__iexact=nombre_dep).exists()

        if existe:
            raise ValidationError("Ya existe este departamento")
        return nombre_dep




