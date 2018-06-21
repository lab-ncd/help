from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lista_cursos, name='lista_cursos'),
    url(r'^pesquisa$', views.pesquisa_turma, name='pesquisa_turma'),
    url(r'^turma/(?P<pk>[0-9]+)/editar_turma$', views.editar_turma, name='editar_turma'),
    url(r'^(?P<slug>[\w_-]+)/$', views.details_curso, name='details_curso'),
    url(r'^turma/(?P<pk>[0-9]+)/$', views.details_turma, name='details_turma'),
    url(r'^turma/(?P<pk>[0-9]+)/remover$', views.remover_turma, name='remover_turma'),
]