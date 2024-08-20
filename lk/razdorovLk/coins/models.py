from django.db import models
from account.models import User
from shop.models import ShopItem

OPERATION_CHOICES = [
    ('plus', 'Получено'),
    ('minus', 'Потрачено'),
]


class History(models.Model):
    """ Модель с историей начислений и списаний бонусов """
    item = models.ForeignKey(ShopItem, models.SET_NULL, null=True, verbose_name='Услуга')
    price = models.IntegerField(verbose_name='Количество токенов')
    method = models.CharField(max_length=11, choices=OPERATION_CHOICES, verbose_name='Метод')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата операции')
    user = models.ForeignKey(User, models.SET_NULL, null=True, verbose_name='Пользователь')

    def __str__(self):
        return self.item.title

    class Meta:
        verbose_name = 'Операцию'
        verbose_name_plural = 'Операции'
