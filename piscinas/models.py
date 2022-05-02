from django.db import models

# Create your models here.
class PiscGrMañana (models.Model):
    pass

class Nombre_Piscina (models.Model):
    nombre_piscina=models.CharField(max_length=300,verbose_name='nombre_piscina', help_text="Nombre de la piscina")


class Valores_Piscina (models.Model):
    nombre_piscina=models.ForeignKey('nombre_piscina',verbose_name='nombre_piscina', help_text="Nombre_Piscina",on_delete=models.CASCADE)
    fecha=models.DateField(auto_now_add=True,verbose_name='Fecha del Registro')
    fecha_Hora=models.DateTimeField(auto_now=True,verbose_name='Fecha y hora del ultimo cambio')
    tecnico=models.CharField(max_length=300,verbose_name='Tecnico', help_text="Nombre del Técnico")
    Ph=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='PiscPh', help_text="Ph")
    cloro_libre=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='Pisc_cloro_Libre', help_text="Cloro Libre")
    cloro_total=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='Pisc_cloro_Total', help_text="Cloro Total",null=True)
    transparencia=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='Pisc_Transparencia', help_text="Transparencia",null=True)
    turbidez=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='PiscGrMañana_turbidez', help_text="turbidez")
    bromo=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='spa_bromo', help_text="Bromo En El SPA")
    temp_agua_spa=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='temp_agua', help_text="temp_agua En El SPA")
    temp_aire_spa=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='temp_aire', help_text="temp_aire En El SPA")
    humedad_aire_spa=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='humedad_aire', help_text="Humedad_aire En El SPA")
    presion_filtro=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='presion_en_filtro', help_text="presion_en_filtro")
    presion_filtro_limpiado=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='presion_en_filtro_limpiado', help_text="presion_en_filtro_limpiado")
    nivel_cloro=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='nivel_cloro', help_text="nivel_cloro")
    nivel_ph=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='nivel_Ph', help_text="nivel_Ph")
    nivel_bromo=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='nivel_bromo', help_text="nivel_bromo")
    rellenado_cloro=models.BooleanField( verbose_name='rellenado_cloro', help_text="rellenado_cloro")
    rellenado_Ph=models.BooleanField( verbose_name='rellenado_Ph', help_text="rellenado_Ph")
    rellenado_bromo=models.BooleanField( verbose_name='rellenado_bromo', help_text="rellenado_bromo")
    limpieza_bordes=models.BooleanField(verbose_name='limpieza_bordes', help_text="limpieza_bordes")
    Incidencias=models.CharField(max_length=300,verbose_name='valores_Incidencias', help_text="Descripción de la Incidencia")
    correctos=models.BooleanField(null=False)
    intervencion_realizada=models.CharField(max_length=300,verbose_name='Intervencion realizada', help_text="Descripción de la Intervencion")
    registrados=models.BooleanField(null=False, default=False)
 