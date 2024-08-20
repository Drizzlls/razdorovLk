from django import template

register = template.Library()

@register.filter(name='checkingForEmptiness')
def checkingForEmptiness(item: str) -> str:
    """ Склонение городов """
    if item:
        return item
    else:
        return 'В ожидании'
