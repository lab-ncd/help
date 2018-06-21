# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, get_user_model
from django.conf import settings
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import PasswordReset
from base.utils import generate_hash_key
from django.contrib import messages

User = get_user_model()

####################### PAINEL DO USUÁRIO ####################### 
@login_required
def painel(request):
	template_name = 'painel.html'
	context = {}
	return render(request, template_name, context)



################## PAINEL DO USUÁRIO - EDIÇÃO ##################
@login_required
def edit(request):
	template_name = 'edit.html'
	context = {}
	post = request.user
	context['post'] = post
	if request.method == 'POST':
		form = EditAccountForm(request.POST, instance=request.user)
		if form.is_valid:
			form.save()
			form = EditAccountForm(instance=request.user)
			context['sucess'] = True
			return redirect('usuarios:painel')

	else:
		form = EditAccountForm(instance=request.user)

	context['form'] = form
	return render(request, template_name, context)

###################### PÁGINA DE EDIÇÃO DE SENHA ######################
@login_required
def edit_password(request):
	template_name = 'edit_password.html'
	context = {}
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			context['success'] = True
	else:
		form = PasswordChangeForm(user=request.user)

	context['form'] = form
	return render(request, template_name, context)

##################### REGISTRO DE USUÁRIO #####################
def register(request):
	template_name = 'cadastro.html'
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			user = authenticate(
				username=user.username, password=form.cleaned_data['password1']
				)
			login(request, user)

			return redirect('base:home')
	else:
		form = RegisterForm()

	context = {
		'form': form
	}
	return render(request, template_name, context)

################## PÁGINA DE ALTERAÇÃO DE SENHA ##################
def password_reset(request):
	template_name = 'password_reset.html'
	context = {}
	form = PasswordResetForm(request.POST or None)
	if form.is_valid():
		form.save()
		context['success'] = True
	context['form'] = form
	return render(request, template_name, context)

############# PÁGINA DE SOLICITAÇÃO DE ALTERAÇÃO DE SENHA #############
def password_reset_confirm(request, key):
	template_name = 'password_reset_confirm.html'
	context = {}
	reset = get_object_or_404(PasswordReset, key=key)
	form = SetPasswordForm(user=reset.user, data=request.POST or None)
	if form.is_valid():
		form.save()
		context['success'] = True
	context['form'] = form
	return render(request, template_name, context)