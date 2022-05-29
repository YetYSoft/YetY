# Generated by Django 4.0.3 on 2022-05-28 21:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('espacios', '0002_alter_amaestramientos_codigo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='amaestramientos',
            name='usuario_maestra',
            field=models.ForeignKey(default=1, help_text='usuario_maestra', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='usuario_maestra', to=settings.AUTH_USER_MODEL),
        ),
    ]
