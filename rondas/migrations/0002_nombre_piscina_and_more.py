# Generated by Django 4.0.3 on 2022-05-01 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rondas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nombre_Piscina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_piscina', models.CharField(help_text='Nombre de la piscina', max_length=300, verbose_name='nombre_piscina')),
            ],
        ),
        migrations.RemoveField(
            model_name='piscgrmañana',
            name='PiscGrMañana_CloroLibre',
        ),
        migrations.RemoveField(
            model_name='piscgrmañana',
            name='PiscGrMañana_CloroTotal',
        ),
        migrations.RemoveField(
            model_name='piscgrmañana',
            name='PiscGrMañana_Fecha',
        ),
        migrations.RemoveField(
            model_name='piscgrmañana',
            name='PiscGrMañana_FechaHora',
        ),
        migrations.RemoveField(
            model_name='piscgrmañana',
            name='PiscGrMañana_Incidencias',
        ),
        migrations.RemoveField(
            model_name='piscgrmañana',
            name='PiscGrMañana_Ph',
        ),
        migrations.RemoveField(
            model_name='piscgrmañana',
            name='PiscGrMañana_Tecnico',
        ),
        migrations.RemoveField(
            model_name='piscgrmañana',
            name='PiscGrMañana_Transparencia',
        ),
        migrations.RemoveField(
            model_name='piscgrmañana',
            name='PiscGrMañana_Turbidez',
        ),
        migrations.CreateModel(
            name='Valores_Piscina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valores_fecha', models.DateField(auto_now_add=True, verbose_name='Fecha del Registro')),
                ('valores_fecha_Hora', models.DateTimeField(auto_now=True, verbose_name='Fecha y hora del ultimo cambio')),
                ('valores_tecnico', models.CharField(help_text='Nombre del Técnico', max_length=300, verbose_name='Tecnico')),
                ('valores_Ph', models.DecimalField(decimal_places=2, help_text='Ph', max_digits=2, verbose_name='PiscPh')),
                ('valores_cloro_libre', models.DecimalField(decimal_places=2, help_text='Cloro Libre', max_digits=2, verbose_name='Pisc_cloro_Libre')),
                ('valores_cloro_total', models.DecimalField(decimal_places=2, help_text='Cloro Total', max_digits=2, null=True, verbose_name='Pisc_cloro_Total')),
                ('valores_transparencia', models.DecimalField(decimal_places=2, help_text='Transparencia', max_digits=2, null=True, verbose_name='Pisc_Transparencia')),
                ('valores_turbidez', models.DecimalField(decimal_places=2, help_text='turbidez', max_digits=2, verbose_name='PiscGrMañana_turbidez')),
                ('valores_bromo', models.DecimalField(decimal_places=2, help_text='Bromo En El SPA', max_digits=2, verbose_name='spa_bromo')),
                ('valores_temp_agua_spa', models.DecimalField(decimal_places=2, help_text='temp_agua En El SPA', max_digits=2, verbose_name='temp_agua')),
                ('valores_temp_aire_spa', models.DecimalField(decimal_places=2, help_text='temp_aire En El SPA', max_digits=2, verbose_name='temp_aire')),
                ('valores_humedad_aire_spa', models.DecimalField(decimal_places=2, help_text='Humedad_aire En El SPA', max_digits=2, verbose_name='humedad_aire')),
                ('valores_presion_filtro', models.DecimalField(decimal_places=2, help_text='presion_en_filtro', max_digits=2, verbose_name='presion_en_filtro')),
                ('valores_presion_filtro_limpiado', models.DecimalField(decimal_places=2, help_text='presion_en_filtro_limpiado', max_digits=2, verbose_name='presion_en_filtro_limpiado')),
                ('valores_nivel_cloro', models.DecimalField(decimal_places=2, help_text='nivel_cloro', max_digits=2, verbose_name='nivel_cloro')),
                ('valores_nivel_ph', models.DecimalField(decimal_places=2, help_text='nivel_Ph', max_digits=2, verbose_name='nivel_Ph')),
                ('valores_nivel_bromo', models.DecimalField(decimal_places=2, help_text='nivel_bromo', max_digits=2, verbose_name='nivel_bromo')),
                ('valores_rellenado_cloro', models.BooleanField(help_text='rellenado_cloro', verbose_name='rellenado_cloro')),
                ('valores_rellenado_Ph', models.BooleanField(help_text='rellenado_Ph', verbose_name='rellenado_Ph')),
                ('valores_rellenado_bromo', models.BooleanField(help_text='rellenado_bromo', verbose_name='rellenado_bromo')),
                ('valores_limpieza_bordes', models.BooleanField(help_text='limpieza_bordes', verbose_name='limpieza_bordes')),
                ('valores_Incidencias', models.CharField(help_text='Descripción de la Incidencia', max_length=300, verbose_name='valores_Incidencias')),
                ('valores_correctos', models.BooleanField()),
                ('valores_intervencion_realizada', models.BooleanField()),
                ('valores_realizado_el_registro', models.BooleanField(default=False)),
                ('valores_nombre_piscina', models.ForeignKey(help_text='Nombre_Piscina', on_delete=django.db.models.deletion.CASCADE, to='rondas.nombre_piscina', verbose_name='nombre_piscina')),
            ],
        ),
    ]
