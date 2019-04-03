from django import template
from django.conf import settings

register = template.Library()


@register.filter(name='hex')
def to_hex(number):
    return hex(number)


if __name__ == '__main__':
    print(hex(1))
