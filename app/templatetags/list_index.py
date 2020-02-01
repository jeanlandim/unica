from django import template
register = template.Library()
# Acessa o elemento da váriavel para certo número
@register.filter
def list_index(var,index):
    return (var[index])
