from cProfile import label
from django import forms
from django.forms import ModelForm,Textarea, ValidationError

from espacios.models import *
from espacios.urls import *
from django.forms import ValidationError
from django.shortcuts import redirect, render



class Nuevo_departamento_form(forms.ModelForm):
    class Meta:
        model = Departamentos
        fields= '__all__'
        #help_texts={'nombre':'What is your favorite fruit?'}
        #print ("/////////////////////")
        #print (form)

    def clean_nombre(self):
        nombre_dep= self.cleaned_data ['nombre']
        nombre_dep=nombre_dep.upper()          #.capitalize()
     #   print ("/////////////////////")
     #   print (nombre)
        existe = Departamentos.objects.filter (nombre__iexact=nombre_dep).exists()

        if existe:
            return
            #raise ValidationError("Ya existe este departamento")
        return nombre_dep




class Planta_o_zona_nueva_form(forms.ModelForm):
    class Meta:
        model = Planta_o_zonas
        fields= '__all__'
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'departamento':forms.CheckboxSelectMultiple(),
        }

        #help_texts={'nombre':'What is your favorite fruit?'}
        #print ("/////////////////////")
        #print (form)

    def clean_nombre(self):
        nombre_zona= self.cleaned_data ['nombre']
        nombre_zona=nombre_zona.upper()          #.capitalize()
        existe = Planta_o_zonas.objects.filter (nombre__iexact=nombre_zona).exists()

        if existe:
            #return redirect('Departamentos_list/')
            print ("Existe /////////////////////")
            raise ValidationError("Ya existe este departamento")
        return nombre_zona

class Planta_o_zona_edit_form(forms.ModelForm):
    class Meta:
        model = Planta_o_zonas
        fields= '__all__'
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'departamento':forms.CheckboxSelectMultiple(),
        }
    def clean_nombre(self):
        nombre_zona= self.cleaned_data ['nombre']
        nombre_zona=nombre_zona.upper()          #.capitalize()
        return nombre_zona


class Hab_cuarto_sala_nueva_form(forms.ModelForm):
    class Meta:
        model = Habs_cuartos_salas
        fields= '__all__'
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'departamento':forms.CheckboxSelectMultiple(),
            'planta_o_zona':forms.CheckboxSelectMultiple(),
        }


    def clean_nombre(self):
        nombre_cuarto= self.cleaned_data ['nombre']
        nombre_cuarto=nombre_cuarto.capitalize()          #.capitalize() upper()
        existe = Habs_cuartos_salas.objects.filter (nombre__iexact=nombre_cuarto).exists()

        if existe:
            raise ValidationError("Ya existe este departamento")
        return nombre_cuarto


class Hab_cuarto_sala_edit_form(forms.ModelForm):
    class Meta:
        model = Habs_cuartos_salas
        fields= '__all__'
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'departamento':forms.CheckboxSelectMultiple(),
            'planta_o_zona':forms.CheckboxSelectMultiple(),
        }

    def clean_nombre(self):
        nombre_cuarto= self.cleaned_data ['nombre']
        nombre_cuarto=nombre_cuarto.capitalize()          #.capitalize() upper()
        return nombre_cuarto




class Puerta_nueva_form(forms.ModelForm):
    class Meta:
        model = Puertas
        fields= '__all__'
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'departamento':forms.CheckboxSelectMultiple(),
            'planta_o_zona':forms.CheckboxSelectMultiple(),
            'cuarto':forms.CheckboxSelectMultiple(),
        }


    def clean_nombre(self):
        nombre_puerta= self.cleaned_data ['nombre']
        nombre_puerta=nombre_puerta.capitalize()          #.capitalize() upper()
        existe = Puertas.objects.filter (nombre__iexact=nombre_puerta).exists()

        if existe:
            raise ValidationError("Ya existe esta puerta")
        return nombre_puerta


class Puerta_edit_form(forms.ModelForm):
    class Meta:
        model = Puertas
        fields= '__all__'
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'departamento':forms.CheckboxSelectMultiple(),
            'planta_o_zona':forms.CheckboxSelectMultiple(),
            'cuarto':forms.CheckboxSelectMultiple(),

        }

    def clean_nombre(self):
        nombre_puerta= self.cleaned_data ['nombre']
        nombre_puerta=nombre_puerta.capitalize()          #.capitalize() upper()
        return nombre_puerta
