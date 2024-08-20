# Generated by Django 5.1 on 2024-08-09 07:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operationName', models.CharField(max_length=150, verbose_name='Название операции')),
                ('price', models.IntegerField(verbose_name='Количество токенов')),
                ('method', models.CharField(choices=[('plus', 'Получено'), ('minus', 'Потрачено')], max_length=11, verbose_name='Метод')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата операции')),
                ('employees', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Операцию',
                'verbose_name_plural': 'Операции',
            },
        ),
    ]
