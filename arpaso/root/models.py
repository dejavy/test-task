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

class BdLog(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    model_name = models.CharField(max_length=50, blank=True, null=True)
    action = models.CharField(max_length=50, blank=True, null=True)

    def  __unicode__(self):
        return '%s' % (self.model_name)

def db_deletes(sender, instance, **kwargs):
    log_unit = BdLog()
    log_unit.model_name = sender
    log_unit.action = 'delete'
    log_unit.save()

def db_changes(sender, instance, created, **kwargs):
    log_unit = BdLog()
    log_unit.model_name = sender.__name__
    if created:
        log_unit.action = 'add'
    else:
        log_unit.action = 'changed'
    log_unit.save()

models.signals.post_save.connect(db_changes, sender=User)
models.signals.post_save.connect(db_changes, sender=Users)
models.signals.post_delete.connect(db_deletes, sender=User)
models.signals.post_delete.connect(db_deletes, sender=Users)