from django import template
from django.urls import translate_url as django_translate_url

register = template.Library()


@register.simple_tag(takes_context=True)
def translate_url(context, lang_code):
    path = context.get('request').build_absolute_uri()
    return django_translate_url(path, lang_code)


@register.simple_tag(takes_context=True)
def current_neutral_url(context):
    path = context.get('request').path
    return '/' + '/'.join(path.split('/')[2:])
