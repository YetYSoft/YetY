# Generated by Django 4.0.3 on 2022-06-16 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0032_alter_parte_prioridad'),
    ]

    operations = [
        migrations.AddField(
            model_name='ot_parte',
            name='fecha_cambio_ot',
            field=models.DateField(auto_now=True, verbose_name='Fecha del ultimo cambio'),
        ),
    ]
