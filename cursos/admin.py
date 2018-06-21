# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Curso, Turma


class CursoAdmin(admin.ModelAdmin):
	
	list_display = ['nome', 'slug', 'created_at', 'updated_at']
	search_fields = ['name', 'slug']
	prepopulated_fields = {'slug': ('nome',)}	

# registrar model + model admin associado
admin.site.register(Curso, CursoAdmin)

class TurmaAdmin(admin.ModelAdmin):
	
	list_display = ['curso', 'codigo', 'professor', 'about']
	search_fields = ['curso', 'codigo', 'professor']

admin.site.register(Turma, TurmaAdmin)