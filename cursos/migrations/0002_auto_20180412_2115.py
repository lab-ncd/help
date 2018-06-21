# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-13 00:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oferta', models.CharField(max_length=25, verbose_name='Oferta')),
                ('professor', models.CharField(max_length=100, verbose_name='Professor')),
                ('vagas_presencial', models.IntegerField(verbose_name='Vagas para lista presencial')),
                ('vagas_lista_espera', models.IntegerField(verbose_name='Vagas para lista de espera')),
                ('about', models.TextField(blank=True, verbose_name='Informa\xe7\xf5es Adicionais')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('inicio', models.DateField(default=datetime.date.today, verbose_name='Data de In\xedcio')),
                ('final', models.DateField(default=datetime.date.today, verbose_name='Data de T\xe9rmino')),
            ],
            options={
                'ordering': ['curso'],
                'verbose_name': 'Turma',
                'verbose_name_plural': 'Turmas',
            },
        ),
        migrations.AlterField(
            model_name='curso',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descri\xe7\xe3o'),
        ),
        migrations.AddField(
            model_name='turma',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.Curso'),
        ),
    ]
