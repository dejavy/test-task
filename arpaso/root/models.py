#coding: utf8
from django.db import models
from django.dispatch import Signal
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User

class Users(models.Model):
#   basic data
    first_name = models.CharField(verbose_name = u'Имя', max_length=50,)
    last_name = models.CharField(verbose_name = u'Фамилия', max_length=50,)
    creation_date = models.DateTimeField(u'Дата и время создание записи', auto_now_add=True)
    birth_date = models.DateField(u'Дата Рождения')

#   secondary data
    biography = models.TextField(verbose_name = u'Биография')
    contacts = models.EmailField(u'Почта')
    
    def  __unicode__(self):
        return '%s' % (self.first_name)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    # Other fields here
    creation_date = models.DateTimeField(u'Дата и время создание записи', auto_now_add=True)
    birth_date = models.DateField(u'Дата Рождения', blank=True, null=True)
#   secondary data
    biography = models.TextField(verbose_name = u'Биография',  blank=True, null=True)

def user_post_delete(sender, instance, **kwargs):
    try:
        UserProfile.objects.get(user=instance).delete()
    except:
        pass

def user_post_save(sender, instance, **kwargs):
    try:
        profile, new = UserProfile.objects.get_or_create(user=instance)
    except:
        pass

models.signals.post_delete.connect(user_post_delete, sender=User)
models.signals.post_save.connect(user_post_save, sender=User)