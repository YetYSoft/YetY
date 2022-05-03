from django.db import models

# Create your models here.
class PiscGrMañana (models.Model):
    pass

class Nombre_Piscina (models.Model):
    nombre_piscina=models.CharField(max_length=300,verbose_name='nombre_piscina', help_text="Nombre de la piscina")


class Valores_Piscina (models.Model):
    valores_nombre_piscina=models.ForeignKey('nombre_piscina',verbose_name='nombre_piscina', help_text="Nombre_Piscina",on_delete=models.CASCADE)
    valores_fecha=models.DateField(auto_now_add=True,verbose_name='Fecha del Registro')
    valores_fecha_Hora=models.DateTimeField(auto_now=True,verbose_name='Fecha y hora del ultimo cambio')
    valores_tecnico=models.CharField(max_length=300,verbose_name='Tecnico', help_text="Nombre del Técnico")
    valores_Ph=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='PiscPh', help_text="Ph")
    valores_cloro_libre=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='Pisc_cloro_Libre', help_text="Cloro Libre")
    valores_cloro_total=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='Pisc_cloro_Total', help_text="Cloro Total",null=True)
    valores_transparencia=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='Pisc_Transparencia', help_text="Transparencia",null=True)
    valores_turbidez=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='PiscGrMañana_turbidez', help_text="turbidez")
    valores_bromo=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='spa_bromo', help_text="Bromo En El SPA")
    valores_temp_agua_spa=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='temp_agua', help_text="temp_agua En El SPA")
    valores_temp_aire_spa=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='temp_aire', help_text="temp_aire En El SPA")
    valores_humedad_aire_spa=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='humedad_aire', help_text="Humedad_aire En El SPA")
    valores_presion_filtro=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='presion_en_filtro', help_text="presion_en_filtro")
    valores_presion_filtro_limpiado=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='presion_en_filtro_limpiado', help_text="presion_en_filtro_limpiado")
    valores_nivel_cloro=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='nivel_cloro', help_text="nivel_cloro")
    valores_nivel_ph=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='nivel_Ph', help_text="nivel_Ph")
    valores_nivel_bromo=models.DecimalField(max_digits=2, decimal_places=2, verbose_name='nivel_bromo', help_text="nivel_bromo")
    valores_rellenado_cloro=models.BooleanField( verbose_name='rellenado_cloro', help_text="rellenado_cloro")
    valores_rellenado_Ph=models.BooleanField( verbose_name='rellenado_Ph', help_text="rellenado_Ph")
    valores_rellenado_bromo=models.BooleanField( verbose_name='rellenado_bromo', help_text="rellenado_bromo")
    valores_limpieza_bordes=models.BooleanField(verbose_name='limpieza_bordes', help_text="limpieza_bordes")

    valores_Incidencias=models.CharField(max_length=300,verbose_name='valores_Incidencias', help_text="Descripción de la Incidencia")
    valores_correctos=models.BooleanField(null=False)
    valores_intervencion_realizada=models.BooleanField(null=False)
    valores_realizado_el_registro=models.BooleanField(null=False, default=False)
