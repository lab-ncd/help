from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^novo$', views.novo, name='novo'), # URL para criar um novo aluno
	url(r'^pesquisa$', views.pesquisa, name='pesquisa'), # URL para pesquisar os alunos
	url(r'^lista$', views.lista, name='lista'), # URL para exibir a lista de alunos salvos
	url(r'^post/(?P<pk>\d+)/edit/$', views.editar, name='editar'), # URL para editar um aluno
	url(r'^aluno/(?P<pk>[0-9]+)/$', views.detalhes, name='detalhes'), # URL para mostrar os detalhes de um aluno
	url(r'^aluno/(?P<pk>[0-9]+)/remover$', views.remover, name='remover'), # URL para remover um aluno
]
