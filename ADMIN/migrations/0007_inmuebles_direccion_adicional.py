# Generated by Django 2.2.1 on 2019-05-17 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ADMIN', '0006_auto_20190516_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmuebles',
            name='direccion_adicional',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
