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




class zona_nueva_form(forms.ModelForm):
    class Meta:
        model = Zonas
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
        existe = Zonas.objects.filter (nombre__iexact=nombre_zona).exists()
        if existe:
            #return redirect('Departamentos_list/')
            print ("Existe /////////////////////")
            raise ValidationError("Ya existe este departamento")
        return nombre_zona


class zona_edit_form(forms.ModelForm):
    class Meta:
        model = Zonas
        fields= '__all__'
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'departamento':forms.CheckboxSelectMultiple(),
        }
    def clean_nombre(self):
        nombre_zona= self.cleaned_data ['nombre']
        nombre_zona=nombre_zona.upper()          #.capitalize()
        return nombre_zona




#############   Ubicaciones ##############



 
class ubicacion_nueva_form(forms.ModelForm):
    class Meta:
        model = Ubicaciones
        fields= '__all__'
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'departamento':forms.CheckboxSelectMultiple(),
            'zona':forms.CheckboxSelectMultiple(),
        }
    def clean_nombre(self):
        nombre_ubicacion= self.cleaned_data ['nombre']
        nombre_ubicacion=nombre_ubicacion.capitalize()          #.capitalize() upper()
        existe = Ubicaciones.objects.filter (nombre__iexact=nombre_ubicacion).exists()
        if existe:
            raise ValidationError("Ya existe este departamento")
        return nombre_ubicacion


class ubicacion_edit_form(forms.ModelForm):
    class Meta:
        model = Ubicaciones
        fields= '__all__'
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'departamento':forms.CheckboxSelectMultiple(),
            'zona':forms.CheckboxSelectMultiple(),
        }
    def clean_nombre(self):
        nombre_ubicacion= self.cleaned_data ['nombre']
        nombre_ubicacion=nombre_ubicacion.capitalize()          #.capitalize() upper()
        return nombre_ubicacion


#############   Elementos ##############


class Elemento_nuevo_form(forms.ModelForm):
    class Meta:
        model = Elementos
        fields= '__all__'
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'departamento':forms.CheckboxSelectMultiple(),
            'zona':forms.CheckboxSelectMultiple(),
            'ubicacion':forms.CheckboxSelectMultiple(),
        }
    def clean_nombre(self):
        nombre_elemento= self.cleaned_data ['nombre']
        nombre_elemento=nombre_elemento.capitalize()          #.capitalize() upper()
        existe = Elementos.objects.filter (nombre__iexact=nombre_elemento).exists()
        if existe:
            raise ValidationError("Ya existe este elemento")
        return nombre_elemento


class Elemento_edit_form(forms.ModelForm):
    class Meta:
        model = Elementos
        fields= '__all__'
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'departamento':forms.CheckboxSelectMultiple(),
            'zona':forms.CheckboxSelectMultiple(),
            'ubicacion':forms.CheckboxSelectMultiple(),
        }
    def clean_nombre(self):
        nombre_elemento= self.cleaned_data ['nombre']
        nombre_elemento=nombre_elemento.capitalize()          #.capitalize() upper()
        return nombre_elemento



#############   Llaves ##############

class llave_nueva_form(forms.ModelForm):
    class Meta:
        model = llaves
        fields= '__all__'
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'zona':forms.CheckboxSelectMultiple(),
            'ubicacion':forms.CheckboxSelectMultiple(),
            'codigo':forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'num_bombillo':forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'maestra':forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'posicion_de_llave_en_armario':forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'usuario_llave':forms.TextInput(attrs={'class':'form-control form-control-lg'}),

        }
    def clean_nombre(self):
        nombre_llave= self.cleaned_data ['nombre']
        nombre_llave=nombre_llave.capitalize()          #.capitalize() upper()
        existe = llaves.objects.filter (nombre__iexact=nombre_llave).exists()
        if existe:
            raise ValidationError("Ya existe esta llave")
        return nombre_llave


class llave_edit_form(forms.ModelForm):
    class Meta:
        model = llaves
        fields= '__all__'
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'departamento':forms.CheckboxSelectMultiple(),
            'zona':forms.CheckboxSelectMultiple(),
            'ubicacion':forms.CheckboxSelectMultiple(),
        }
    def clean_nombre(self):
        nombre_llave= self.cleaned_data ['nombre']
        nombre_llave=nombre_llave.capitalize()          #.capitalize() upper()
        return nombre_llave
