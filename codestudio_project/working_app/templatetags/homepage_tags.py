from django.template import Library
from django.template.defaultfilters import stringfilter

register = Library()

'''Кастомный шаблон для замены запятой на точку (для координат)'''
def comma_replacer(value):
    return value

comma_replacer = stringfilter(comma_replacer)

register.filter(comma_replacer)