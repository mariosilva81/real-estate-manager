from django import template
from babel.numbers import format_currency

register = template.Library()


@register.filter
def currency_brl(value):
    return format_currency(value, "BRL", locale="pt_BR")
