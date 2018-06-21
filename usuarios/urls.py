from django.conf.urls import url
from .views import *
from django.contrib.auth import views

urlpatterns = [
    url(r'^$', views.login,
    {'template_name': 'login.html'}, name='login'),
    url(r'^sair/$', views.logout,
    {'next_page': 'base:home'}, name='logout'),
    url(r'^cadastre-se$', register, name='register'),
    url(r'^painel$', painel, name='painel'),
    url(r'^editar$', edit, name='edit'),
    url(r'^nova-senha$', edit_password, name='edit_password'),
    url(r'^recuperar_senha$', password_reset, name='password_reset'),
    url(r'^confirmar_nova_senha/(?P<key>\w+)$', password_reset_confirm, name='password_reset_confirm'),
]