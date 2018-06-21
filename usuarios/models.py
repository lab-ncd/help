# -*- coding: utf-8 -*-

######################## MAKING THE NECESSARY IMPORTS ############################

from __future__ import unicode_literals
import re
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core import validators
from django.conf import settings

##################################################################################


############### Model de Equipe #######################################

############################################################################


################################# Model de Usuário #####################################

class User(AbstractBaseUser, PermissionsMixin):

	username = models.CharField(
		'Nome de Usuário', max_length=30, unique=True,
		validators = [validators.RegexValidator(re.compile('^[\w.@+-]+$'),
			'Apenas são permitidos letras, números ou os caracteres: @ . + - _', 'invalid')]
		)
	email = models.EmailField('E-mail', help_text='Digite seu email criado pelo NCD', unique=True)
	name = models.CharField('Nome', max_length=100, blank=True)
	#equipe = models.CharField(max_length=100, choices=Equipe.choices)
	is_active = models.BooleanField('Está Ativo?', blank=True, default=True)
	is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
	date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

	objects = UserManager()

	USERNAME_FIELD = 'username' #Campo que é utilizado para logar
	REQUIRED_FIELDS = ['email'] #Campo chave para superusuário

	#Representação string do usuário
	def __str__(self):
		return self.name or self.username

	def get_short_name(self):
		return self.username

	def get_full_name(self):
		return str(self)

	class Meta:
		verbose_name = 'Usuário'
		verbose_name_plural = 'Usuários'

##################################################################################


######################### Model Para Recuperação de senha ########################

class PasswordReset(models.Model):

	user = models.ForeignKey(
		settings.AUTH_USER_MODEL, verbose_name='Usuário',
		related_name='resets'
		)
	key = models.CharField('Chave', max_length=100, unique=True)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	confirmed = models.BooleanField('Confirmado', default=False, blank=True)

	def __str__(self):
		return '{0} em {1}'.format(self.user, self.created_at)

	class Meta:
		verbose_name = 'Nova Senha'
		verbose_name_plural = 'Novas Senhas'
		ordering = ['-created_at']

###################################################################################