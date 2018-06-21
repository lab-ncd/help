# -*- coding: utf-8 -*-

################# MAKING THE NECESSARY IMPORTS #################

from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from aluno.models import Aluno
import sys # Corrigir problema de acentuação
reload(sys) # Corrigir problema de acentuação
sys.setdefaultencoding('utf8') # Corrigir problema de acentuação


##################### View de Cursos #####################
### View para renderizar uma lista com todos os cursos cadastrados
@login_required
def lista_cursos(request):
	cursos = Curso.objects.all() # Pega todos os objetos
	context = {}
	context['cursos'] = cursos
	return render(request, 'lista_cursos.html', context)

##################### View de Pesquisa de turmas #####################
# View utilizada para pesquisar uma ou mais turmas
@login_required
def pesquisa_turma(request): 
    turmas = Turma.objects.order_by('codigo')
    context = {}
    query = request.GET.get("pesquisa")
    context['query'] = query
    if query:
        turmas = (turmas.filter(codigo__icontains=query)) or (turmas.filter(professor__icontains=query))
        context['turmas'] = turmas
    return render(request, 'pesquisa_turma.html', context)

############## View de detalhamento do Curso ##############
# View utilizada para detalhar o curso e utilizada para fazer
# o cadastro de uma turma 
@login_required
def details_curso(request, slug):
	cursos = get_object_or_404(Curso, slug=slug)
	context = {}
	context['cursos'] = cursos	

	if request.method == "POST":
		form = Cadastro_Turma(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.curso = Curso.objects.get(slug=slug)
			post.codigo = request.POST.get("codigo")
			post.professor = request.POST.get("professor")
			post.vagas_presencial = request.POST.get("vagas_presencial")
			post.vagas_lista_espera = request.POST.get("vagas_lista_espera")
			post.about = request.POST.get("about")
			post.inicio = request.POST.get("inicio")
			post.final = request.POST.get("final")
			post.save()
			return redirect('cursos:details_turma', pk=post.pk)
	else:
		form = Cadastro_Turma()

	context['form'] = form
	turmas = Turma.objects.filter(curso__slug=slug)
	context['turmas'] = turmas

	return render(request, 'details_curso.html', context)

############## View utilizada para editar uma turma ##############
# View que recupera uma turma do banco de dados de acordo com a "pk"
# e renderiza a turma para a edição 
@login_required
def editar_turma(request, pk):
	template_name = 'editar_turma.html'
	context = {}
	post = get_object_or_404(Turma, pk=pk)
	context['post'] = post
	if request.method == 'POST':
		form = Cadastro_Turma(request.POST, instance=post)
		if form.is_valid():
			form.save()
			form = Cadastro_Turma(instance=post)
			return redirect('cursos:details_turma', pk=post.pk)
	else:
		form = Cadastro_Turma(instance=post)

	context['form'] = form

	return render(request, template_name, context)

############## View para incrementar horas faltadas ##############
# View utilizada para incrementar as horas faltadas em uma turma para 
# todos os alunos da mesma
def incrementa_horas(turmas,horas):

	if horas:
		for it in turmas.pauta.all():
			it.horas_faltadas = it.horas_faltadas + int(horas.pop(0))
			it.save()

############## View para criar pauta ##############
# View utilizada para criar uma relação de um aluno com as horas
# faltadas pelo mesmo em uma turma
def cria_pauta(turma, aluno):
    pauta = HorasFaltadas()
    pauta.aluno = aluno
    pauta.horas_faltadas = 0
    pauta.save()
    turma.pauta.add(pauta)

############## View para remover um aluno de uma turma ##############
# View auxiliar utilizada para remover um ou mais alunos de uma turma
def remove_aluno(request, query, turmas):
	for a in query:
			aluno = Aluno.objects.get(pk=a)
			turmas.alunos_inscritos.remove(aluno)
			for it in turmas.pauta.all():
				if it.aluno == aluno:
					turmas.pauta.remove(it)
					messages.success(request,  aluno.nome +' foi removido da turma ' + turmas.curso.nome + '-' + turmas.codigo)

############## View para remover um aluno de uma lista de espera para uma turma ##############
# View auxiliar utilizada para remover um ou mais alunos da lista de espera
def remove_aluno_espera(request, mover, turmas):
	for b in mover:
			aluno = Aluno.objects.get(pk=b)
			turmas.alunos_espera.remove(aluno)
			messages.success(request,  aluno.nome +' foi removido da lista de espera da turma ' + turmas.curso.nome + '-' + turmas.codigo)

############## View para mover um aluno de uma lista de espera para uma turma ##############
# View auxiliar utilizada para mover um ou mais alunos da lista de espera
# para uma turma
def mover_aluno(request, mover, turmas):
	for b in mover:
			aluno = Aluno.objects.get(pk=b)

			if(turmas.alunos_inscritos.count() < turmas.vagas_presencial):
				turmas.alunos_espera.remove(aluno)
				turmas.alunos_inscritos.add(aluno)
				cria_pauta(turmas,aluno)
				messages.success(request,  aluno.nome +' foi movido para a turma ' + turmas.curso.nome + '-' + turmas.codigo)
			else:
				messages.warning(request, 'Turma ' + turmas.curso.nome + '-' + turmas.codigo + ' cheia, o aluno(a) ' + aluno.nome + ' permaneceu na lista de espera')


############## View para vizualizar os detalhes de uma turma ##############
# View utilizada para renderizar uma turma
# View utilizada para remover o aluno de uma turma
# View utilizada para mover um aluno da lista de espera para a turma
# View que atualiza a pauta
@login_required
def details_turma(request, pk):
	context = {}
	turmas = get_object_or_404(Turma, pk=pk)
	context['turmas'] = turmas
	alunos = turmas.alunos_inscritos.all()
	context['alunos'] = alunos
	espera = turmas.alunos_espera.all()
	context['espera'] = espera
	query = request.GET.getlist("a")
	horas = request.GET.getlist("h")
	mover = request.GET.getlist("e")
	botao_mover = request.GET.get("mover")
	botao_remover = request.GET.get("remover")
	incrementa_horas(turmas,horas)

	try:
		if query: # Se query for verdadeiro é pq tem aluno pra ser removido
			remove_aluno(request, query, turmas)
		if botao_mover: # Se botao_mover for verdadeiro é pq tem aluno pra ser movido		
			mover_aluno(request, mover, turmas)
		elif botao_remover: # Se bota_remover for verdadeiro é pq tem aluno pra ser removido da lista de espera
			remove_aluno_espera(request, mover, turmas)
			
	except Aluno.DoesNotExist:
		aluno = None
	return render(request, 'details_turma.html', context)


############### View de remocao de uma turma ##############
# View que remove uma turma de acordo com a "pk"
@login_required
def remover_turma(request, pk): # Funcao para remover uma turma
    turma = get_object_or_404(Turma, pk=pk)
    slug = turma.curso.slug
    turma.delete()
    return redirect('cursos:details_curso', slug=slug)