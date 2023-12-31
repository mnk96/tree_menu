# Generated by Django 2.2.19 on 2023-10-28 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название меню')),
                ('url', models.SlugField(max_length=255, verbose_name='Ссылка на меню')),
            ],
            options={
                'verbose_name': 'Меню',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название пункта меню')),
                ('url', models.SlugField(max_length=255, verbose_name='Ссылка на пункт меню')),
                ('menu', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='app_menu.Menu')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='app_menu.Item')),
            ],
            options={
                'verbose_name': 'Пункт меню',
                'verbose_name_plural': 'Пункты меню',
            },
        ),
    ]
