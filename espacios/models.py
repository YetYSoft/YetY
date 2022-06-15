
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

 
class llaves (models.Model):
    nombre=models.CharField( default='0' ,null=False,max_length=50,verbose_name='Puerta de la ubicacion', help_text="Puerta de la ubicacion",blank=True)
    zona=models.ManyToManyField('Zonas',  max_length=50,verbose_name='acceso desde zona',  help_text="acceso desde zona", blank=True)
    ubicacion=models.ManyToManyField('Ubicaciones', default='0' ,max_length=50,verbose_name='Llave de la ubicacion', help_text="Llave de la ubicacion",blank=True)

    codigo=models.CharField(default='0',max_length=50,verbose_name='codigo de la ubicacion', help_text="codigo de la ubicacion",blank=True)
    num_bombillo=models.IntegerField   (default= 0,verbose_name='numero de bombillo', help_text="Numero de bombillo",blank=True)
    maestra=models.ManyToManyField('Amaestramientos',max_length=50,verbose_name='Amaestramientos', help_text="Amaestramientos", blank=True)
    posicion_de_llave_en_armario=models.CharField(default='0',max_length=50,verbose_name='ubicacion en el armario', help_text="ubicacion en el armario",blank=True)
    usuario_llave=models.ForeignKey(User,related_name="usuario_llave",default=1,on_delete=models.PROTECT,null=True, blank=False,help_text="usuario_llave") 
    def __str__(self):
        return '{}'.format(self.nombre)
    class Meta:
        ordering = ["nombre"]

class Amaestramientos (models.Model):
  
    nombre=models.CharField(default='SSTT' ,max_length=50,verbose_name='nombre_amaestramiento', help_text="nombre_amaestramiento",blank=True)
    codigo=models.CharField(default='0',max_length=50,verbose_name='codigo de la ubicacion', help_text="codigo de la ubicacion",blank=True)
    usuario_maestra=models.ForeignKey(User,related_name="usuario_maestra",default=1,on_delete=models.PROTECT,null=True, blank=False,help_text="usuario_maestra") 

    def __str__(self):
        return '{}'.format(self.nombre)
    class Meta:
            ordering = ["nombre"]

 
class Elementos (models.Model):
    nombre=models.CharField(default='' ,null=False,max_length=50,verbose_name='Equipo o instalacion', help_text="Equipo o instalacion",blank=True)
    ubicacion=models.ManyToManyField('Ubicaciones',  max_length=50,verbose_name='acceso a ...',  help_text="acceso a ..." , blank=True)
    zona=models.ManyToManyField('Zonas',  max_length=50,verbose_name='acceso desde zona',  help_text="acceso desde zona" , blank=True)
    departamento=models.ManyToManyField('Departamentos',  max_length=50,verbose_name='departamento de',  help_text="departamento de" ,blank=True)
    def __str__(self):
        return '{}'.format(self.nombre)
    class Meta:
            ordering = ["nombre"]
 

class Ubicaciones(models.Model):
    nombre=models.CharField(default='' ,null=False,max_length=50,verbose_name='Nombre de la ubicacion', help_text="Nombre de la zona",blank=True)
    zona=models.ManyToManyField('Zonas',  max_length=50,verbose_name='acceso desde zona',  help_text="acceso desde zona", blank=True)
    departamento=models.ManyToManyField('Departamentos',  max_length=50,verbose_name='departamento de',  help_text="departamento de", blank=True)
    alojamiento=models.BooleanField(default= False,  verbose_name='Habitacion?',  help_text="Habitacion?") 
    AyB=models.BooleanField(default= False,  verbose_name='AyB?',  help_text="AyB?") 
    General=models.BooleanField(default= False,  verbose_name='General?',  help_text="General?") 
    otro=models.BooleanField(default= False,  verbose_name='Otro?',  help_text="Otro?") 
    def __str__(self):
        return '{}'.format(self.nombre)
    class Meta:
            ordering = ["nombre"]
            

class Zonas (models.Model):
    nombre=models.CharField(default='' ,null=False,max_length=50,verbose_name='Nombre de la zona', help_text="Nombre de la ubicacion",blank=True)
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

 