# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-10 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0009_auto_20180403_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='nivel_conhecimento',
        ),
        migrations.AddField(
            model_name='aluno',
            name='celular',
            field=models.CharField(default=b'', max_length=12),
        ),
        migrations.AddField(
            model_name='aluno',
            name='complemento',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='aluno',
            name='estado',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='aluno',
            name='nivelamento',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='aluno',
            name='sexo',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]