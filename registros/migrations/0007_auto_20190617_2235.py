# Generated by Django 2.2.1 on 2019-06-17 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0006_auto_20190617_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ot_pedido_material',
            name='estado_ot',
            field=models.CharField(choices=[('Aprobado', 'Aprobado'), ('En Curso', 'En Curso'), ('En espera', 'En espera'), ('Inversion', 'Inversion'), ('Pedido', 'Pedido'), ('Rechazado', 'Rechazado')], default='Pendiente', max_length=30),
        ),
    ]
