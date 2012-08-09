# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from .models import Users, User

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
