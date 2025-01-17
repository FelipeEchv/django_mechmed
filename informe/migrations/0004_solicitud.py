# Generated by Django 4.1.2 on 2024-07-18 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informe', '0003_alter_presupuesto_año_vehiculo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id_solicitud', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_cliente_sol', models.CharField(max_length=60)),
                ('telefono_cliente_sol', models.CharField(max_length=20)),
                ('correo_cliente_sol', models.EmailField(max_length=254)),
            ],
        ),
    ]
