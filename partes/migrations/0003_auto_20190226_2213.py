# Generated by Django 2.1.5 on 2019-02-26 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0002_auto_20190226_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ot_parte',
            name='ubicacion_ot',
            field=models.ForeignKey(help_text='Numero de Habitación o ubicación', max_length=30, null=True, on_delete=django.db.models.deletion.CASCADE, to='partes.Ot_Ubicaciones', verbose_name='Ubicación'),
        ),
    ]
