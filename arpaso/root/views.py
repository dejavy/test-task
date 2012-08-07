#coding: utf8
from django.db.models import Q
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson
from django.shortcuts import redirect

from .models import Users

def home(request, template='home.html'):
	return TemplateResponse(request, template, {'test'})

