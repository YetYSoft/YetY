from mailbox import NoSuchMailboxError
from django.db import models
from django.contrib.auth.models import User
from espacios.models import Ubicaciones, Elementos
# Create your models here.
 


class Parte (models.Model):
    ubicacion=models.ForeignKey('espacios.Ubicaciones',max_length=40,verbose_name='Ubicación', help_text="Numero de Habitación o ubicación",on_delete=models.SET_NULL,null=True)
    elemento =models.ForeignKey('espacios.Elementos',  max_length=40,verbose_name='Elemento',  help_text="Elemento, Objeto o Aparato",      on_delete=models.SET_NULL,null=True)
    descripcion=models.CharField(max_length=300,verbose_name='Descripción', help_text="Descripción del problema")
    prioridad=models.ForeignKey('Prioridad',max_length=30, default=3, blank=True,  null=True, on_delete=models.SET_NULL)
    estado=models.ForeignKey ('Estados',max_length=30,default='Pendiente',null=True,on_delete=models.SET_NULL)
    recusos_propios=models.BooleanField(default= True,  verbose_name='Recursos propios',  help_text="Recursos propios") 
    pedido =models.ForeignKey('Pedido',  max_length=40,verbose_name='num_pedido',  help_text="num_pedido",      on_delete=models.SET_NULL,null=True)
    notas=models.CharField(default='',max_length=30, blank=True, help_text="Poner una nota a este parte") #        falta por definir (Nota para relacionar)
    Usuario=models.ForeignKey(User,related_name="Usuario",default=1,on_delete=models.SET_NULL, null=True,blank=True,help_text="usuario que ha hecho este parte") 
    Tecnico_asignado=models.ForeignKey(User,related_name="Tecnico",default=1,on_delete=models.SET_NULL, null=True,blank=True, help_text="Tecnico que tiene este parte") 
    Tecnico_fin_parte=models.ForeignKey(User,related_name="Tecnico_fin_parte",default=1,on_delete=models.SET_NULL, null=True,blank=True,  help_text="Tecnico que tiene este parte") 
    fecha_parte=models.DateField(auto_now_add=True,verbose_name='Fecha del parte')
    fecha_hora_cambio=models.DateTimeField(auto_now=True,verbose_name='Fecha y hora del ultimo cambio')
    fecha_hora_terminado=models.DateTimeField(null=True,blank=True, verbose_name='Fecha y hora de la terminacion del parte', )
    def __str__(self):
        #"""String for representing the Model object (in Admin site etc.)"""
        return '{}'.format(self.pk)
    class Meta:
        ordering = ["-pk"]


class Trabajos(models.Model):
    num_parte_tra=models.ForeignKey('Parte',verbose_name='Num de parte', help_text="Num de parte",on_delete=models.SET_NULL,null=True)
    descripcion_tra=models.CharField(max_length=300,verbose_name='Descripción', help_text="Descripción del Trabajo")
    fecha_tra=models.DateField(auto_now_add=True,verbose_name='Fecha del trabajo')
    fecha_cambio_tra=models.DateField(auto_now=True,verbose_name='Fecha del ultimo cambio')
    fecha_hora_cambio_tra=models.DateTimeField(auto_now=True,verbose_name='Fecha y hora del ultimo cambio')
    tecnico_tra=models.ForeignKey(User,related_name="tecnico_tra",default=1,on_delete=models.SET_NULL, null=True,blank=False,help_text="usuario que ha hecho este trabajo") 
    def __str__(self):
        #"""String for representing the Model object (in Admin site etc.)"""
        return '{}'.format(self.pk)
    class Meta:
        ordering = ["-pk"]

class Pedido (models.Model):
    num_pedido=models.IntegerField   (default= 0,verbose_name='num_pedido', help_text="num_pedido",blank=True)
    nombre_empresa=models.CharField( default='' ,null=False,max_length=50,verbose_name='nombre_empresa', help_text="nombre_empresa",blank=True)
    descrip_trabajo=models.CharField( default='' ,null=False,max_length=50,verbose_name='nombre_empresa', help_text="nombre_empresa",blank=True)
    def __str__(self):
        #"""String for representing the Model object (in Admin site etc.)"""
        return '{}'.format(self.num_pedido)
    class Meta:
        ordering = ["-num_pedido"]


class Prioridad(models.Model):
    prioridades=models.CharField(max_length=30, blank=False, null=False)
    def __str__(self):
        #"""String for representing the Model object (in Admin site etc.)"""
        return '{}'.format(self.pk)
    class Meta:
        ordering = ["-pk"]


class Estados(models.Model):
    estados=models.CharField(max_length=30, blank=False, null=True)
    def __str__(self):
        #"""String for representing the Model object (in Admin site etc.)"""
        return '{}'.format(self.pk)
    class Meta:
        ordering = ["-pk"]





##################          Viejo Partes    ################ 

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
    #id=models.IntegerField()
    ubicacion_ub=models.CharField(primary_key=True, max_length=30)
    class Meta:
        ordering = ['ubicacion_ub']
    def __str__(self):
        return '{}'.format(self.ubicacion_ub)

class Ot_Elementos(models.Model):
    elemento_el=models.CharField(primary_key=True, max_length=30)
    elemento_en_hab=models.BooleanField(default= False,  verbose_name='Está en hab?',  help_text="Está en hab?") 
    elemento_en_AyB=models.BooleanField(default= False,  verbose_name='Está en AyB?',  help_text="Está en AyB?") 
    elemento_en_varios=models.BooleanField(default= False,  verbose_name='Está en varios?',  help_text="Está en varios?") 
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
