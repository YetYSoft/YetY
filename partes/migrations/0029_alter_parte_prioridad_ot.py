# Generated by Django 4.0.3 on 2022-06-15 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0028_estados_parte_pedido_prioridad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parte',
            name='prioridad_ot',
            field=models.ForeignKey(blank=True, default=3, max_length=30, null=True, on_delete=django.db.models.deletion.SET_NULL, to='partes.prioridad'),
        ),
    ]
