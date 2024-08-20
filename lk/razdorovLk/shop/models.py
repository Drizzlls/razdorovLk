from django.db import models
from account.models import User

class ShopItem(models.Model):
    """ Модель с услугами в магазине """
    title = models.CharField(max_length=150, null=False, verbose_name='Название услуги')
    description = models.CharField(max_length=300, null=False, verbose_name='Краткое описание услуги')
    price = models.IntegerField(null=False, verbose_name='Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'



