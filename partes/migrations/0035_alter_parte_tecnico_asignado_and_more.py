# Generated by Django 4.0.3 on 2022-06-16 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('partes', '0034_alter_pedido_descrip_trabajo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parte',
            name='Tecnico_asignado',
            field=models.ForeignKey(blank=True, default=0, help_text='Tecnico que tiene este parte', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Tecnico', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='parte',
            name='Tecnico_fin_parte',
            field=models.ForeignKey(blank=True, default=0, help_text='Tecnico que tiene este parte', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Tecnico_fin_parte', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='parte',
            name='pedido',
            field=models.ForeignKey(default=0, help_text='num_pedido', max_length=40, null=True, on_delete=django.db.models.deletion.SET_NULL, to='partes.pedido', verbose_name='num_pedido'),
        ),
        migrations.AlterField(
            model_name='parte',
            name='prioridad',
            field=models.ForeignKey(blank=True, default=4, max_length=30, null=True, on_delete=django.db.models.deletion.SET_NULL, to='partes.prioridad'),
        ),
    ]
