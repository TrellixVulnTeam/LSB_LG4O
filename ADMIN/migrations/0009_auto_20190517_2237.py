# Generated by Django 2.2.1 on 2019-05-18 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ADMIN', '0008_ciudades_departamentos_paises'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ciudades',
            old_name='ciudad',
            new_name='nombre',
        ),
    ]
