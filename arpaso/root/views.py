#coding: utf8
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect

from django import forms
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout

from django.db import connection


from .models import Users

@login_required
def home(request, template='home.html'):
	users = Users.objects.all()
	#print users, connection.queries
	return TemplateResponse(request, template, {'usershtml': users})

def settings(request, template='settings.html'):
    return TemplateResponse(request, template, {})

def password(request, template='registration/change.html'):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        print request.user
        form = PasswordChangeForm(request.user)
    return TemplateResponse(request, template, {'form': form,})


def edit(request, template='registration/change.html'):
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        print request.user
        user = User.objects.get(username=request.user)
        form = UserChangeForm(instance=user)
    return TemplateResponse(request, template, {'form': form,})

def registration(request, template='registration/register.html'):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return TemplateResponse(request, template, {'form': form,})

def logout(request):
    auth.logout(request)
    # Перенаправление на страницу.
    return HttpResponseRedirect("/")
