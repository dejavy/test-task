# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserChangeForm
from django.forms import ModelForm
from django import forms
from .models import Users, User, UserProfile
from .widgets import CalendarWidget

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('birth_date', 'biography')
        exclude = ('user', 'username')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

        self.fields['birth_date'].widget = CalendarWidget()