from django.core.exceptions import ObjectDoesNotExist
from .workingWithCoins import MethodsWithCoins
from account.models import User
from shop.models import ShopItem
from tasks.models import Tasks
from django.core.exceptions import ObjectDoesNotExist
from history import HistoryCoins

class CoinsForTasks(MethodsWithCoins, HistoryCoins):
    """ Класс для работы с коинами из заданий """

    def __init__(self, user, idItem):
        self.user = user
        self.idItem = idItem
        self.item = self.getItemFromModel()
        self.coinsUser = self.getCoinsUser()


    def minusCoins(self) -> bool:
        try:
            self.user.coins -= self.item.price
            self.user.save()
        except Exception as e:
            print('Логи: ошибка в изменении количество коинов за покупку в магазине', e)
        return True

    def plusCoins(self):
        pass

    def getItemFromModel(self):
        try:
            return ShopItem.objects.get(pk=self.idItem)
        except ObjectDoesNotExist:
            print('Логи: Такого айтема нет в базе')
            raise ObjectDoesNotExist('Такого айтема нет')
        except Exception as e:
            print('Логи: Другая ошибка', e)
            raise ValueError(f'Ошибка — {e}')

    def getCoinsUser(self):
        if self.user.coins < self.item.price:
            print(f'Логи: Пользователю {self.user} выдана ошибка, что недостаточно баллов')
            raise ValueError('Недостаточно баллов')
        else:
            return True

    def addIntoHistory(self):
        try:
            History.objects.create(operationName=self.item.title,
                                   price=self.item.price,
                                   method='minus',
                                   user=self.user)
        except Exception as e:
            print('Ошибка записи в историю', e)
