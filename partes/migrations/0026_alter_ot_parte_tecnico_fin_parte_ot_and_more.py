# Generated by Django 4.0.3 on 2022-05-14 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('partes', '0025_ot_parte_tecnico_fin_parte_ot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ot_parte',
            name='Tecnico_fin_parte_ot',
            field=models.ForeignKey(blank=True, default=1, help_text='Tecnico que tiene este parte', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Tecnico_fin_parte_ot', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ot_parte',
            name='Tecnico_ot',
            field=models.ForeignKey(blank=True, default=1, help_text='Tecnico que tiene este parte', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Tecnico_ot', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ot_parte',
            name='Usuario_ot',
            field=models.ForeignKey(blank=True, default=1, help_text='usuario que ha hecho este parte', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Usuario_ot', to=settings.AUTH_USER_MODEL),
        ),
    ]