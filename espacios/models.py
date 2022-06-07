
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class llaves (models.Model):
    nombre=models.CharField( default='0' ,null=False,max_length=50,verbose_name='Puerta de la sala o lugar', help_text="Puerta de la sala o lugar",blank=True)
    codigo=models.CharField(default='0',max_length=50,verbose_name='codigo de la sala o lugar', help_text="codigo de la sala o lugar",blank=True)
    maestra=models.ManyToManyField('Amaestramientos',max_length=50,verbose_name='Amaestramientos', help_text="Amaestramientos", blank=True)
    planta_o_zona=models.ManyToManyField('Planta_o_zonas',  max_length=50,verbose_name='acceso desde planta_o_zona',  help_text="acceso desde planta_o_zona", blank=True)
    posicion_de_llave_en_armario=models.CharField(default='0',max_length=50,verbose_name='ubicacion en el armario', help_text="ubicacion en el armario",blank=True)
    usuario_llave=models.ForeignKey(User,related_name="usuario_llave",default=1,on_delete=models.PROTECT,null=True, blank=False,help_text="usuario_llave") 
    def __str__(self):
        return '{}'.format(self.nombre)
    class Meta:
            ordering = ["nombre"]

class Amaestramientos (models.Model):
  
    nombre=models.CharField(default='SSTT' ,max_length=50,verbose_name='nombre_amaestramiento', help_text="nombre_amaestramiento",blank=True)
    codigo=models.CharField(default='0',max_length=50,verbose_name='codigo de la sala o lugar', help_text="codigo de la sala o lugar",blank=True)
    usuario_maestra=models.ForeignKey(User,related_name="usuario_maestra",default=1,on_delete=models.PROTECT,null=True, blank=False,help_text="usuario_maestra") 

    def __str__(self):
        return '{}'.format(self.nombre)
    class Meta:
            ordering = ["nombre"]

 
class Puertas (models.Model):
    nombre=models.CharField(default='' ,null=False,max_length=50,verbose_name='Puerta de la sala o lugar', help_text="Puerta de la sala o lugar",blank=True)
    cuarto=models.ManyToManyField('Habs_cuartos_salas',  max_length=50,verbose_name='acceso a ...',  help_text="acceso a ..." , blank=True)
    planta_o_zona=models.ManyToManyField('Planta_o_zonas',  max_length=50,verbose_name='acceso desde planta_o_zona',  help_text="acceso desde planta_o_zona" , blank=True)
    departamento=models.ManyToManyField('Departamentos',  max_length=50,verbose_name='departamento de',  help_text="departamento de" ,blank=True)
    def __str__(self):
        return '{}'.format(self.nombre)
    class Meta:
            ordering = ["nombre"]


class Habs_cuartos_salas(models.Model):
    nombre=models.CharField(default='' ,null=False,max_length=50,verbose_name='Nombre de la sala o lugar', help_text="Nombre de la planta o zona",blank=True)
    planta_o_zona=models.ManyToManyField('Planta_o_zonas',  max_length=50,verbose_name='acceso desde planta_o_zona',  help_text="acceso desde planta_o_zona", blank=True)
    departamento=models.ManyToManyField('Departamentos',  max_length=50,verbose_name='departamento de',  help_text="departamento de", blank=True)
    def __str__(self):
        return '{}'.format(self.nombre)
    class Meta:
            ordering = ["nombre"]

class Planta_o_zonas (models.Model):
    nombre=models.CharField(default='' ,null=False,max_length=50,verbose_name='Nombre de la planta o zona', help_text="Nombre de la sala o lugar",blank=True)
    departamento=models.ManyToManyField('Departamentos',  max_length=50,verbose_name='departamento de',  help_text="departamento de" ,blank=True)
    def __str__(self):
        return '{}'.format(self.nombre)
    class Meta:
            ordering = ["nombre"]


class Departamentos (models.Model):
    nombre=models.CharField(default='' ,null=False,max_length=50,verbose_name='Nombre del departamento', blank=False)
    def __str__(self):
        return '{}'.format(self.nombre)
    class Meta:
            ordering = ["nombre"]

