from django import forms
from .models import *

class Cadastro_Turma(forms.ModelForm):
	
	class Meta:
		model = Turma
		fields = ('codigo', 'professor', 'vagas_presencial', 'vagas_lista_espera',
			'about', 'inicio', 'final')
