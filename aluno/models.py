from django.db import models
from django.utils import timezone

class Aluno(models.Model):
	nome = models.CharField(max_length=100)
	nascimento = models.DateField()
	cpf = models.CharField(max_length=11, unique = True)
	genero = models.CharField(max_length=20, default = '')
	telefone = models.CharField(max_length=12, blank = True)
	celular = models.CharField(max_length=12, default = '', blank = True)
	email = models.EmailField(max_length=100, default = '', blank = True)
	data_entrada = models.DateTimeField(default=timezone.now)
	rua = models.CharField(max_length=100, default = '')	
	bairro = models.CharField(max_length=100, default = '')
	cidade = models.CharField(max_length=100, default = '')
	estado = models.CharField(max_length=100, default = '')
	complemento = models.CharField(max_length=100, default = '', blank = True)
	numero_matricula = models.CharField(max_length=20, default='')
	nivelamento = models.CharField(max_length=100, default='')

	def publish(self):
		self.data_entrada = timezone.now()
		self.save()

	def __str__(self):
		return self.nome
