from django.db import models

# Create your models here.
from partes.models import Ot_Ubicaciones



#-----------------Temperaturas -------------



class Ot_Temp_Clima_Interior(models.Model):
    num_Temp_Clima=models.AutoField(primary_key=True, verbose_name='numero de Temp', help_text="numero de orden de Temp")
    field = models.ForeignKey("partes.Ot_Ubicaciones", verbose_name="Ubicacion", related_name="Ot_Temp_Clima_Interior",on_delete=models.SET_NULL,null=True)
    fecha_hora_cambio_ot=models.DateTimeField(auto_now=True, verbose_name='Fecha y hora del ultimo cambio')

    Temp_Impulsion_Aire=models.DecimalField(max_digits=4, decimal_places=2)
    Temp_Retorno_Aire=models.DecimalField(max_digits=4, decimal_places=2)
    Temp_Ambiente=models.DecimalField(max_digits=4, decimal_places=2)

    Temp_Impulsion_Agua_Caliente=models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    Temp_Retorno_Agua_Caliente=models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    Temp_Impulsion_Agua_Fria=models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    Temp_Retorno_Agua_Fria=models.DecimalField(max_digits=4, decimal_places=2, blank=True)

    Caudal_de_aire=models.DecimalField(default=0.0, max_digits=4, decimal_places=2, blank=True)

    notas_ot=models.CharField(default='',max_length=30, blank=True, help_text="Poner una nota")
    #   Modificado por...........


class Ot_Temp_Minibar(models.Model):
    fecha_hora_cambio_ot=models.DateTimeField(auto_now=True,verbose_name='Fecha y hora del ultimo cambio')
    field = models.ForeignKey("partes.Ot_Ubicaciones", verbose_name="Ubicacion minibar", related_name="Ot_Temp_Minibar",on_delete=models.SET_NULL,null=True)
    Temp_Interior=models.DecimalField(max_digits=4, decimal_places=2)
    #   Modificado por...........

class Ot_Pedido_material(models.Model):
    num_Pedido=models.AutoField(primary_key=True)
    fecha_hora_cambio_ot=models.DateTimeField(auto_now=True,verbose_name='Fecha y hora del ultimo cambio')
    Material=models.CharField(default='',max_length=60, blank=True, help_text="Poner una nota")
    notas_ot=models.CharField(default='',max_length=300, blank=True, help_text="Poner una nota")
    ESTADOS_DE_PEDIDO=[ ('Aprobado','Aprobado'),('En Curso','En Curso'),('En espera','En espera'),("Inversion","Inversion"),('Pedido','Pedido'), ("Rechazado","Rechazado")]
    estado_ot=models.CharField (max_length=30,default='Pendiente', choices=ESTADOS_DE_PEDIDO)
    #   Modificado por...........
