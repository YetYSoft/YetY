# Generated by Django 2.1.4 on 2019-03-03 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0004_auto_20190226_2226'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ot_elementos',
            options={'ordering': ['elemento_el']},
        ),
        migrations.AlterModelOptions(
            name='ot_ubicaciones',
            options={'ordering': ['ubicacion_ub']},
        ),
    ]
