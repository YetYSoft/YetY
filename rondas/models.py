from django.db import models

# Create your models here.


class PiscGrMañana (models.Model):
    PiscGrMañana_Tecnico=models.CharField(max_length=300,verbose_name='Tecnico', help_text="Nombre del Técnico", default='David')
    PiscGrMañana_Fecha=models.DateField(auto_now_add=True,verbose_name='Fecha del Registro')
    PiscGrMañana_FechaHora=models.DateTimeField(auto_now=True,verbose_name='Fecha y hora del ultimo cambio')
    PiscGrMañana_Ph=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='PiscGrMañana_Ph', help_text="Ph")
    PiscGrMañana_CloroLibre=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='PiscGrMañana_Libre', help_text="Cloro Libre")
    PiscGrMañana_CloroTotal=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='PiscGrMañana_Total', help_text="Cloro Total",null=True)
    PiscGrMañana_Transparencia=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='PiscGrMañana_Transparencia', help_text="Transparencia",null=True, default=1)
    PiscGrMañana_Turbidez=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='PiscGrMañana_Turbidez', help_text="Turbidez", default=1)
    PiscGrMañana_Incidencias=models.CharField(max_length=300,verbose_name='PiscGrMañana_Incidencias', help_text="Descripción de la Incidencia")
