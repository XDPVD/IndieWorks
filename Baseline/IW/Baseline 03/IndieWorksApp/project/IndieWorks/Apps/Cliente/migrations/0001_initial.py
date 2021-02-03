# Generated by Django 3.1.5 on 2021-02-03 06:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=35)),
                ('apellido_paterno', models.CharField(max_length=15)),
                ('apellido_materno', models.CharField(max_length=15)),
                ('dni', models.CharField(max_length=8, validators=[django.core.validators.MinLengthValidator(8)])),
                ('correo', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=9, validators=[django.core.validators.MinLengthValidator(7)])),
                ('rating', models.FloatField(default=0)),
                ('distrito', models.CharField(max_length=20)),
                ('cuenta', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
