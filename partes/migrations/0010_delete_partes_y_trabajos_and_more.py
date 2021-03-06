# Generated by Django 4.0.3 on 2022-05-13 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0009_partes_y_trabajos'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Partes_y_trabajos',
        ),
        migrations.AddField(
            model_name='ot_parte',
            name='fecha_hora_terminado_ot',
            field=models.DateTimeField(null=True, verbose_name='Fecha y hora de la terminacion del parte'),
        ),
        migrations.AlterField(
            model_name='ot_etiquetas',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ot_pedidos',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
