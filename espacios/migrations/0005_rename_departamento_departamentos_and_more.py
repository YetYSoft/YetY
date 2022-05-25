# Generated by Django 4.0.3 on 2022-05-21 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('espacios', '0004_alter_planta_o_zona_departamento'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Departamento',
            new_name='Departamentos',
        ),
        migrations.RenameModel(
            old_name='Planta_o_zona',
            new_name='Planta_o_zonas',
        ),
        migrations.AlterModelOptions(
            name='amaestramientos',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='departamentos',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='habs_cuartos_salas',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='llaves',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='planta_o_zonas',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='puertas',
            options={'ordering': ['nombre']},
        ),
        migrations.AddField(
            model_name='amaestramientos',
            name='usuario_maestra',
            field=models.ForeignKey(default=1, help_text='usuario_maestra', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuario_maestra', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='llaves',
            name='usuario_llave',
            field=models.ForeignKey(default=1, help_text='usuario_llave', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuario_llave', to=settings.AUTH_USER_MODEL),
        ),
    ]