from django import template

register = template.Library()


@register.filter
def has_group(user, grupo):
    return user.groups.filter(name=grupo).exists()
