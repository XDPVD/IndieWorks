# Generated by Django 3.1.5 on 2021-02-03 17:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cliente', '0001_initial'),
        ('Trabajador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('distrito', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('telefono', models.CharField(max_length=9, validators=[django.core.validators.MinLengthValidator(7)])),
                ('categoria', models.CharField(max_length=15)),
                ('precio', models.FloatField(default=0)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('1', 'Publicado'), ('2', 'Solicitado'), ('3', 'Terminado')], default='1', max_length=15)),
                ('rating', models.FloatField(default=0)),
                ('cliente', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Cliente.cliente')),
                ('trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trabajador.trabajador')),
            ],
        ),
    ]
