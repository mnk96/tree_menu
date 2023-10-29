from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название меню')
    url = models.SlugField(max_length=255, verbose_name='Ссылка на меню')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class Item(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название пункта меню')
    url = models.SlugField(max_length=255, verbose_name='Ссылка на пункт меню')
    menu = models.ForeignKey(Menu, blank=True, related_name='items',
                             on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
