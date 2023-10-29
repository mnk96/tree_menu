from django import template
from django.utils.safestring import mark_safe

from app_menu.models import Item, Menu

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    print('trwea ', menu_name)
    menu = Menu.objects.get(url=menu_name)
    menu_id = menu.id
    menu_items = Item.objects.filter(menu=menu_id)
    print('получено: ', menu_items)
    return mark_safe(render_menu(menu_items))


def render_menu(menu_items):
    result = '<ul>'
    print(menu_items)
    for item in menu_items:
        print(item)
        if item.name not in result:
            result += '<li>'
            result += f'<a href="{item.url}">{item.name}</a>'
            print(result)
            result += '</li>'
            if item.children.exists():
                result += render_menu(item.children.all())
    result += '</ul>'
    print(result)
    return result
