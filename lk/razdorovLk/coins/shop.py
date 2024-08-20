from django.core.exceptions import ObjectDoesNotExist
from .workingWithCoins import MethodsWithCoins
from account.models import User
from shop.models import ShopItem
from tasks.models import Tasks
from django.core.exceptions import ObjectDoesNotExist
from .history import HistoryCoins
import logging

logger = logging.getLogger('site')

class CoinsForShop(MethodsWithCoins, HistoryCoins):
    """ Класс для работы с коинами из магазина """

    def __init__(self, user, idItem):
        self.user = user
        self.idItem = idItem
        self.item = self.getItemFromModel()
        self.coinsUser = self.getCoinsUser()


    def minusCoins(self) -> bool:
        try:
            self.user.coins -= self.item.price
            self.user.save()
            self.addIntoHistory()
        except Exception as e:
            logger.error(f'Клиент {self.user.pk} получил ошибку при попытке потратить бонусы.\nОшибка:{e}'
                            f'\nКлиент: {self.user.pk}')
        return True

    def plusCoins(self):
        pass

    def getItemFromModel(self):
        try:
            return ShopItem.objects.get(pk=self.idItem)
        except ObjectDoesNotExist:
            logger.error(f'Клиент {self.user.pk} Пытался потратить бонусы в магазине, но такой услуги не было. '
                         f'ID не найденной услуги: {self.idItem}')
            raise ObjectDoesNotExist('Услуга не найдена. Обратитесь в поддержку.')
        except Exception as e:
            logger.error(f'Ошибка при попытке оплатить услугу у клиента: {self.user.pk}. '
                         f'Пытался получить услугу: {self.idItem}. Ошибка: {e}')
            raise ValueError(f'Ошибка — {e}')

    def getCoinsUser(self):
        if self.user.coins < self.item.price:
            logger.error(
                f'Клиенту {self.user.pk} выдана ошибка, что недостаточно баллов. Текущее количество баллов: {self.user.coins}. Пытался потратить: {self.item.price}. Услуга: {self.idItem}')
            raise ValueError('Недостаточно баллов.\nЕсли это ошибка, то обратитесь в поддержку!')
        else:
            return True

    def addIntoHistory(self):
        self.addHistory(item=self.item,
                        price=self.item.price,
                        method='minus',
                        user=self.user)
