# Generated by Django 4.0.3 on 2022-05-14 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0021_remove_ot_pedidos_usuario_pe_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ot_parte',
            name='borrame_ot',
            field=models.CharField(blank=True, default='', help_text='Poner una nota a este parte', max_length=30),
        ),
    ]
