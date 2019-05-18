# Generated by Django 2.2.1 on 2019-05-16 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adjuntos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programa', models.CharField(blank=True, max_length=100, null=True)),
                ('id_asociado', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('extension', models.CharField(blank=True, max_length=20, null=True)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('mime_type', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contratos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('representante', models.CharField(blank=True, max_length=100, null=True)),
                ('cliente_propietario', models.CharField(blank=True, max_length=100, null=True)),
                ('inmueble', models.IntegerField(blank=True, null=True)),
                ('cliente_arrendatario', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_contrato', models.DateField(blank=True, null=True)),
                ('fecha_inicio', models.DateField(blank=True, null=True)),
                ('fecha_vigencia', models.DateField(blank=True, null=True)),
                ('precio_canon', models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True)),
                ('servicios_arrendador', models.CharField(blank=True, max_length=255, null=True)),
                ('servicios_arrendatario', models.CharField(blank=True, max_length=255, null=True)),
                ('codeudor1', models.CharField(blank=True, max_length=100, null=True)),
                ('codeudor2', models.CharField(blank=True, max_length=100, null=True)),
                ('codeudor3', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gastos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programa', models.CharField(blank=True, max_length=20, null=True)),
                ('id_asociado', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImagenesInmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_asociado', models.IntegerField(blank=True, null=True)),
                ('ubicacion', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inmuebles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('representante', models.CharField(blank=True, max_length=100, null=True)),
                ('cliente_propietario', models.CharField(blank=True, max_length=100, null=True)),
                ('pais', models.CharField(blank=True, max_length=100, null=True)),
                ('departamento', models.CharField(blank=True, max_length=100, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=100, null=True)),
                ('zona', models.CharField(blank=True, max_length=100, null=True)),
                ('barrio', models.CharField(blank=True, max_length=100, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo_inmueble', models.CharField(blank=True, max_length=100, null=True)),
                ('numero_habitaciones', models.IntegerField(blank=True, null=True)),
                ('numero_banos', models.IntegerField(blank=True, null=True)),
                ('numero_parqueaderos', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('latitud', models.CharField(blank=True, max_length=100, null=True)),
                ('longitud', models.CharField(blank=True, max_length=100, null=True)),
                ('estado', models.CharField(blank=True, max_length=100, null=True)),
                ('costo_canon', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('precio_canon', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('tipo_oferta', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_persona', models.CharField(blank=True, max_length=100, null=True)),
                ('asesor', models.CharField(blank=True, max_length=100, null=True)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_identificacion', models.CharField(blank=True, max_length=100, null=True)),
                ('identificacion', models.CharField(blank=True, max_length=100, null=True)),
                ('lugar_expedicion_identificacion', models.CharField(blank=True, max_length=100, null=True)),
                ('pais', models.CharField(blank=True, max_length=100, null=True)),
                ('departamento', models.CharField(blank=True, max_length=100, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=100, null=True)),
                ('direccion', models.CharField(blank=True, max_length=200, null=True)),
                ('telefono_movil', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono_fijo', models.CharField(blank=True, max_length=100, null=True)),
                ('correo', models.CharField(blank=True, max_length=200, null=True)),
                ('valoracion', models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True)),
                ('fecha_creacion', models.DateTimeField(blank=True, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
