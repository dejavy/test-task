#coding: utf8
from django.db import models
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