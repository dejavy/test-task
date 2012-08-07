#coding: utf8
from django.contrib import admin
from root.models import Users

class UsersAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'birth_date', 'biography', 'contacts') 

admin.site.register(Users, UsersAdmin,)