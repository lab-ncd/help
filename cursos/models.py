# -*- coding: utf-8 -*-

################# MAKING THE NECESSARY IMPORTS ################

from __future__ import unicode_literals
from django.db import models
from django.conf  import settings
import datetime
from aluno.models import Aluno

################################################################


############### Modelo de Gerenciamento de Curso ###############

class Gerenciador_de_Curso(models.Manager):

	def search(self, query):
		return self.get_queryset().filter(
			models.Q(nome__icontains=query) | \
			models.Q(description__icontains=query)
			)

#################################################################



######################## Modelo de Curso ########################

class Curso(models.Model):

	nome = models.CharField('Nome', max_length=100)
	# O campo slug será utilizado como complemento da URL
	# Ex.: mysite.com/cursos/Nome_da_Slug
	slug = models.SlugField('Atalho')
	description = models.TextField('Descrição', blank=True)

	created_at = models.DateTimeField(
		'Criado em', auto_now_add=True
		)

	updated_at = models.DateTimeField(
		'Atualizado em', auto_now=True
		)

	objects = Gerenciador_de_Curso()

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = 'Curso'
		verbose_name_plural = 'Cursos'
		ordering = ['created_at']

#################################################################

class HorasFaltadas(models.Model):
	aluno = models.ForeignKey(Aluno)
	horas_faltadas = models.IntegerField(default=0)


######################## Modelo das Turmas ######################

class Turma(models.Model):

	curso = models.ForeignKey(Curso)
	codigo = models.CharField('Código', max_length=25, default='None', unique=True)
	professor = models.CharField('Professor', max_length=100)
	vagas_presencial = models.IntegerField('Vagas para lista presencial')
	vagas_lista_espera = models.IntegerField('Vagas para lista de espera')
	about = models.TextField('Informações Adicionais', blank=True)
	created_at = models.DateTimeField(
		'Criado em', auto_now_add=True
		)
	inicio = models.DateField("Data de Início", default=datetime.date.today)
	final = models.DateField("Data de Término", default=datetime.date.today)
	alunos_inscritos = models.ManyToManyField(Aluno, related_name='%(class)s_Aluno_inscrito')
	alunos_espera = models.ManyToManyField(Aluno, related_name='%(class)s_Aluno_espera')
	pauta = models.ManyToManyField(HorasFaltadas, related_name='%(class)s_Pauta')

	def __str__(self):
		return self.codigo

	class Meta:
		verbose_name = 'Turma'
		verbose_name_plural = 'Turmas'
		ordering = ['created_at']

#################################################################