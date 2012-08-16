#coding: utf8
from django import template
from django.core.urlresolvers import reverse
from django.core import urlresolvers
from django.contrib.contenttypes.models import ContentType

from arpaso.root.models import Users

import datetime

register = template.Library()

@register.tag(name="current_time")
def do_current_time(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, format_string = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
    if not (format_string[0] == format_string[-1] and format_string[0] in ('"', "'")):
        raise template.TemplateSyntaxError("%r tag's argument should be in quotes" % tag_name)
    return CurrentTimeNode(format_string[1:-1])

class CurrentTimeNode(template.Node):
    def __init__(self, format_string):
        self.format_string = format_string
    def render(self, context):
        return datetime.datetime.now().strftime(self.format_string)


@register.tag
def edit_url(parser, token):
    token = token.split_contents()
    obj = token.pop(1)
    return RenderEditUrl(obj)

class RenderEditUrl(template.Node):
    def __init__(self, obj):
        self.obj = template.Variable(obj)

    def render(self, context):
        obj = self.obj.resolve(context)
        print obj.id
        path = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.module_name), args=(obj.id,))
        return u'<a href="%s">%s</a>' % (path, obj)

@register.simple_tag
def get_edit_link(context):
    obj = ContentType.objects.get_for_model(context.__class__)
    url_edit = urlresolvers.reverse("admin:%s_%s_change" % (obj.app_label, obj.model), args=(context.id,))
    return u'<a href="%s">%s</a>' % (url_edit, context)