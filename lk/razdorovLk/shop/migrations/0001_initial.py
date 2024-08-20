# Generated by Django 5.1 on 2024-08-08 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShopItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название услуги')),
                ('description', models.CharField(max_length=300, verbose_name='Краткое описание услуги')),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
        ),
    ]
