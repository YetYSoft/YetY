# Generated by Django 4.0.3 on 2022-05-14 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('partes', '0024_ot_pedidos_usuario_pe_ot_trabajos_usuario_tra'),
    ]

    operations = [
        migrations.AddField(
            model_name='ot_parte',
            name='Tecnico_fin_parte_ot',
            field=models.ForeignKey(default=1, help_text='Tecnico que tiene este parte', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Tecnico_fin_parte_ot', to=settings.AUTH_USER_MODEL),
        ),
    ]
