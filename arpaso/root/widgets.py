#coding: utf8
from django import forms
from django.conf import settings

class CalendarWidget(forms.widgets.DateInput):
    class Media:
        js = (
            settings.STATIC_URL + 'js/jquery-ui-1.8.17.custom.min.js',
            settings.STATIC_URL + 'js/calendar.js',
            )
    def __init__(self, attrs={'class' : 'datepicker'}):
        super(CalendarWidget, self).__init__(attrs=attrs)
