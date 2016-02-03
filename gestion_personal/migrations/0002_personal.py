# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-03 00:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestion_personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=20)),
                ('apellidos', models.CharField(blank=True, max_length=20)),
                ('dni', models.CharField(max_length=9, verbose_name='DNI')),
                ('f_nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de naciemiento')),
                ('direccion', models.CharField(blank=True, max_length=30)),
                ('localidad', models.CharField(blank=True, max_length=20)),
                ('cod_postal', models.CharField(blank=True, max_length=5, null=True, verbose_name='Código postal')),
                ('telefono', models.CharField(blank=True, max_length=12, null=True)),
                ('num_seg_social', models.CharField(blank=True, max_length=12, null=True, verbose_name='Número seguridad social')),
                ('sexo', models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer'), ('Sin especificar', 'Sin especificar')], default='Sin especificar', max_length=16)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='personal/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]