from django import template

register = template.Library()

@register.filter(name='model_type')
def model_type(obj):
    """Возвращает имя класса модели"""
    return obj.__class__.__name__