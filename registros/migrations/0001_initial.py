# Generated by Django 2.2.1 on 2019-06-11 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partes', '0008_ot_trabajos_fecha_hora_cambio_tra'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ot_Pedido_material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora_cambio_ot', models.DateTimeField(auto_now=True, verbose_name='Fecha y hora del ultimo cambio')),
                ('Material', models.CharField(blank=True, default='', help_text='Poner una nota', max_length=60)),
                ('notas_ot', models.CharField(blank=True, default='', help_text='Poner una nota', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Ot_Temp_Minibar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora_cambio_ot', models.DateTimeField(auto_now=True, verbose_name='Fecha y hora del ultimo cambio')),
                ('Temp_Interior', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Ot_Temp_Clima_Interior',
            fields=[
                ('num_Temp_Clima', models.AutoField(help_text='numero de orden de trabajo', primary_key=True, serialize=False, verbose_name='numero de Ot')),
                ('fecha_hora_cambio_ot', models.DateTimeField(auto_now=True, verbose_name='Fecha y hora del ultimo cambio')),
                ('Temp_Impulsion_Aire', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Temp_Retorno_Aire', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Temp_Ambiente', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Temp_Impulsion_Agua_Caliente', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Temp_Retorno_Agua_Caliente', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Temp_Impulsion_Agua_Fria', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Temp_Retorno_Agua_Fria', models.DecimalField(decimal_places=2, max_digits=4)),
                ('notas_ot', models.CharField(blank=True, default='', help_text='Poner una nota', max_length=30)),
                ('field', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Ot_Temp_Clima_Interior', to='partes.Ot_Ubicaciones', verbose_name='my_model1')),
            ],
        ),
    ]