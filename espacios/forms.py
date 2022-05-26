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
        #help_texts={'nombre':'What is your favorite fruit?'}
        #print ("/////////////////////")
        #print (form)

    def clean_nombre(self):
        nombre_dep= self.cleaned_data ['nombre']
        nombre_dep=nombre_dep.capitalize()
     #   print ("/////////////////////")
    #    print (nombre)
        existe = Departamentos.objects.filter (nombre__iexact=nombre_dep).exists()

        if existe:
            raise ValidationError("Ya existe este departamento")
        return nombre_dep




