from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class llaves (models.Model):
    nombre=models.CharField(max_length=30,verbose_name='Puerta de la sala o lugar', help_text="Puerta de la sala o lugar",null=True,blank=True)
    codigo=models.CharField(max_length=30,verbose_name='codigo de la sala o lugar', help_text="codigo de la sala o lugar",null=True,blank=True)
    amaestramiento=models.ManyToManyField('Amaestramientos',max_length=30,verbose_name='Amaestramientos', help_text="Amaestramientos", blank=True)
    planta_o_zona=models.ManyToManyField('Planta_o_zonas',  max_length=30,verbose_name='acceso desde planta_o_zona',  help_text="acceso desde planta_o_zona", blank=True)
    posicion_de_llave_en_armario=models.CharField(max_length=30,verbose_name='ubicacion en el armario', help_text="ubicacion en el armario",null=True,blank=True)
    usuario_llave=models.ForeignKey(User,related_name="usuario_llave",default=1,on_delete=models.SET_NULL, null=True,blank=False,help_text="usuario_llave") 
    class Meta:
            ordering = ["nombre"]

class Amaestramientos (models.Model):
    nombre=models.CharField(max_length=30,verbose_name='nombre_amaestramiento', help_text="nombre_amaestramiento",null=True,blank=True)
    codigo=models.CharField(max_length=30,verbose_name='codigo de la sala o lugar', help_text="codigo de la sala o lugar",null=True,blank=True)
    usuario_maestra=models.ForeignKey(User,related_name="usuario_maestra",default=1,on_delete=models.SET_NULL, null=True,blank=False,help_text="usuario_maestra") 
    class Meta:
            ordering = ["nombre"]


class Puertas (models.Model):
    nombre=models.CharField(max_length=30,verbose_name='Puerta de la sala o lugar', help_text="Puerta de la sala o lugar",null=True,blank=True)
    planta_o_zona=models.ManyToManyField('Planta_o_zonas',  max_length=30,verbose_name='acceso desde planta_o_zona',  help_text="acceso desde planta_o_zona" , blank=True)
    departamento=models.ManyToManyField('Departamentos',  max_length=30,verbose_name='departamento de',  help_text="departamento de" ,blank=True)
    class Meta:
            ordering = ["nombre"]


class Habs_cuartos_salas(models.Model):
    nombre=models.CharField(max_length=30,verbose_name='Nombre de la sala o lugar', help_text="Nombre de la planta o zona",null=True,blank=True)
    planta_o_zona=models.ManyToManyField('Planta_o_zonas',  max_length=30,verbose_name='acceso desde planta_o_zona',  help_text="acceso desde planta_o_zona", blank=True)
    departamento=models.ManyToManyField('Departamentos',  max_length=30,verbose_name='departamento de',  help_text="departamento de", blank=True)
    class Meta:
            ordering = ["nombre"]

class Planta_o_zonas (models.Model):
    nombre=models.CharField(max_length=30,verbose_name='Nombre de la planta o zona', help_text="Nombre de la sala o lugar",null=True,blank=True)
    departamento=models.ManyToManyField('Departamentos',  max_length=30,verbose_name='departamento de',  help_text="departamento de" ,blank=True)
    class Meta:
            ordering = ["nombre"]


class Departamentos (models.Model):
    nombre=models.CharField(max_length=30,verbose_name='Nombre del departamento', null=True,blank=True)
    class Meta:
            ordering = ["nombre"]

