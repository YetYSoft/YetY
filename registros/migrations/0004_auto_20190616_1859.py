# Generated by Django 2.2.1 on 2019-06-16 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0003_auto_20190616_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ot_temp_clima_interior',
            name='num_Temp_Clima',
            field=models.AutoField(help_text='numero de orden de Temp', primary_key=True, serialize=False, verbose_name='numero de Temp'),
        ),
    ]
