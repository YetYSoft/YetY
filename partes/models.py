from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Ot_Parte(models.Model):
    num_ot=models.AutoField(primary_key=True, verbose_name='numero de Ot', help_text="numero de orden de trabajo")
    ubicacion_ot=models.ForeignKey('Ot_Ubicaciones',max_length=30,verbose_name='Ubicación', help_text="Numero de Habitación o ubicación",on_delete=models.SET_NULL,null=True)
    elemento_ot =models.ForeignKey('Ot_Elementos',  max_length=30,verbose_name='Elemento',  help_text="Elemento, Objeto o Aparato",      on_delete=models.SET_NULL,null=True)
    descripcion_ot=models.CharField(max_length=300,verbose_name='Descripción', help_text="Descripción del problema")
    fecha_ot=models.DateField(auto_now_add=True,verbose_name='Fecha del parte')
    fecha_cambio_ot=models.DateField(auto_now=True,verbose_name='Fecha del ultimo cambio')
    fecha_hora_cambio_ot=models.DateTimeField(auto_now=True,verbose_name='Fecha y hora del ultimo cambio')
    fecha_hora_terminado_ot=models.DateTimeField(null=True,blank=True, verbose_name='Fecha y hora de la terminacion del parte', )
    PRIORIDADES=(('1','Urgente') ,('2','Provoca daños') , ('3','Molesta al cliente' ), ('4', 'Mala imagen' ),('5','Legal'))
    prioridad_ot=models.CharField(max_length=30, blank=True, default='1',choices=PRIORIDADES)
    ESTADOS_DE_OT=[ ('Pendiente','Pendiente'),('En Curso','En Curso'),('Terminado','Terminado'), ("Inversion","Inversion"), ('En espera','En espera'), ("Otro","Otro")]
    estado_ot=models.CharField (max_length=30,default='Pendiente', choices=ESTADOS_DE_OT)
    RECURSOS_PROP_O_EXT=[('Propios','Recursos Propios'), ('externos','Recursos externos'),('mixtos','mixtos') ]
    recursos_ot=models.CharField (max_length=30,default='Propios', choices=RECURSOS_PROP_O_EXT)#(Recursos propios o externos)
    etiqueta_ot=models.CharField( default='',blank=True, max_length=30,help_text="Poner una etiqueta a este parte")
    notas_ot=models.CharField(default='',max_length=30, blank=True, help_text="Poner una nota a este parte") #        falta por definir (Nota para relacionar)
    CORRECTIVO_PREVENTIVO_LEGAL_SERVICIO=[('Correctivo','Correctivo'),('Preventivo','Preventivo'),('Legal','Legal'),('Servicio o Ayuda','Servicio o Ayuda'),('Atencion cliente','Atencion cliente')]
    tipo_aviso_ot=models.CharField(max_length=30,default='Correctivo',choices=CORRECTIVO_PREVENTIVO_LEGAL_SERVICIO) # correctivo, preventivo, servicio
    Usuario_ot=models.ForeignKey(User,related_name="Usuario_ot",default=1,on_delete=models.SET_NULL, null=True,blank=True,help_text="usuario que ha hecho este parte") 
    Tecnico_ot=models.ForeignKey(User,related_name="Tecnico_ot",default=1,on_delete=models.SET_NULL, null=True,blank=True, help_text="Tecnico que tiene este parte") 
    Tecnico_fin_parte_ot=models.ForeignKey(User,related_name="Tecnico_fin_parte_ot",default=1,on_delete=models.SET_NULL, null=True,blank=True,  help_text="Tecnico que tiene este parte") 
    borrame_ot=models.CharField(default='',max_length=30, blank=True, help_text="Poner una nota a este parte") #        falta por definir (Nota para relacionar)

    def __str__(self):
        #"""String for representing the Model object (in Admin site etc.)"""
        return '{}'.format(self.num_ot)
    class Meta:
        ordering = ["-num_ot"]
 
class Ot_Trabajos(models.Model):
    num_tra=models.AutoField(primary_key=True,verbose_name='Numero TRA', help_text="Numero de Trabajo")
    num_ot_tra=models.ForeignKey('Ot_Parte',verbose_name='Num de parte', help_text="Num de parte",on_delete=models.CASCADE)
    descripcion_tra=models.CharField(max_length=300,verbose_name='Descripción', help_text="Descripción del Trabajo")
    fecha_tra=models.DateField(auto_now_add=True,verbose_name='Fecha del trabajo')
    fecha_cambio_tra=models.DateField(auto_now=True,verbose_name='Fecha del ultimo cambio')
    fecha_hora_cambio_tra=models.DateTimeField(auto_now=True,verbose_name='Fecha y hora del ultimo cambio')
    Usuario_tra=models.ForeignKey(User,related_name="Usuario_tra",default=1,on_delete=models.SET_NULL, null=True,blank=False,help_text="usuario que ha hecho este trabajo") 
   
    def __str__(self):
        return '{}'.format(self.num_tra)
    class Meta:
        ordering = ["-fecha_cambio_tra"]

class Ot_Ubicaciones(models.Model):
    ubicacion_ub=models.CharField(primary_key=True, max_length=30)
    class Meta:
        ordering = ['ubicacion_ub']
    def __str__(self):
        return '{}'.format(self.ubicacion_ub)

class Ot_Elementos(models.Model):
    elemento_el=models.CharField(primary_key=True, max_length=30)
    class Meta:
        ordering = ["elemento_el"]
    def __str__(self):
        return '{}'.format(self.elemento_el)

class Ot_Etiquetas(models.Model):
    etiqueta_et=models.CharField( default='',blank=True, max_length=30,verbose_name='Etiqueta', help_text="Poner una etiqueta a este parte")

class Ot_Pedidos(models.Model):
    producto_pe=models.CharField(default='',max_length=30,verbose_name='Ele', help_text="Obj")
    Usuario_pe=models.ForeignKey(User,related_name="Usuario_pe",default=1,on_delete=models.SET_NULL, null=True,blank=False,help_text="usuario que ha hecho este Pedido") 





















#-----------------Temperaturas -------------

#class Ot_Temp_Clima interior ():
#        Ubicacion,
#        fecha,
#        temperatura de: impulsion, retorno y ambiente

#class Ot_Temp_Minibar():
#        Ubicacion,
#        fecha,
#        Temperatura de: botella en el interior

#-----------------PISCINAS---------------------

#class Ot_SPA():
# cloro,  fecha fecha_cambio, hora registro, hora cambio

#class Ot_Jacuzzy():
# cloro, bromo, fecha fecha_cambio, hora registro, hora cambio

#class Ot_Piscina():
# cloro, bromo, fecha fecha_cambio, hora registro, hora cambio

#class Ot_Piscina():
# cloro, bromo, fecha fecha_cambio, hora registro, hora cambio

#-----------------Maquinaria---------------------

# Acumuladores, enfriadoras, calderas
#   grados, hora registro, hora cambio
