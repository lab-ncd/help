from django import forms
from .models import Aluno
from cursos.models import *

class PostForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = ('nome', 'nascimento', 'cpf', 'genero', 'telefone', 'celular', 'email', 'rua', 'bairro', 'cidade', 'estado', 'complemento', 'nivelamento')
    
        
class newUserRegistration(forms.Form):
	nome = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'id':'register-form-name', 'name':'register-form-name', 'value':"", 'class':'form-control'}))

class Escolha1(forms.ModelForm):

    class Meta:
        model = Curso
        fields = ('nome',)

class Escolha2(forms.ModelForm):

    class Meta:
        model = Turma
        fields = ('codigo',)