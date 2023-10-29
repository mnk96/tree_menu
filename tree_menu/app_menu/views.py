from django.shortcuts import render

from app_menu.models import Menu


def index(request):
    return render(request, 'app_menu/index.html',
                  {'menus_name': Menu.objects.all()})


def draw_menu(request, path):
    slug = (path.split('/'))
    return render(request, 'app_menu/menu.html', {'menu_name': slug[0]})
