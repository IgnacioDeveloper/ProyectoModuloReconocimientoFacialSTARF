# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-05 18:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mr', '0005_aula'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camara',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=16)),
                ('descripcion', models.CharField(max_length=65)),
                ('aula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mr.Aula')),
            ],
        ),
    ]
