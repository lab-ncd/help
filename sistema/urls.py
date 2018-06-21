from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)), # Url para pagina de admin
    url(r'^', include('base.urls', namespace='base', app_name = 'base')),
    url(r'^aluno/', include('aluno.urls', namespace='aluno', app_name = 'aluno')),
    url(r'^usuario/', include('usuarios.urls', namespace='usuarios', app_name = 'usuarios')),
    url(r'^cursos/', include('cursos.urls', namespace='cursos', app_name = 'cursos'))
]
