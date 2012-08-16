#coding: utf8
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from root.models import Users, UserProfile, BdLog

class UsersAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'birth_date', 'biography', 'contacts') 

admin.site.unregister(User)

class UserProfileinline(admin.StackedInline):
    model = UserProfile

class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileinline]

class BdLogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'model_name', 'action') 


admin.site.register(User, UserProfileAdmin)
admin.site.register(Users, UsersAdmin,)
admin.site.register(BdLog, BdLogAdmin)