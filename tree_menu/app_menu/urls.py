from django.urls import path

from app_menu.views import draw_menu, index

app_name = 'app_menu'

urlpatterns = [
    path('', index, name='main_menu'),
    path('<path:path>/', draw_menu, name='draw_menu'),
]
