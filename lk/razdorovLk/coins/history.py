from .models import History
import logging

logger = logging.getLogger('site')


class HistoryCoins:

    def addHistory(self, item, price: int, method: str, user):
        """
        :param item: Услуга из модели (ShopItem)
        :param price: int(Стоимость услуги)
        :param method: str(Метод (отнять или прибавить))
        :param user: Юзер из модели (User)
        :return: True
        """
        try:
            History.objects.create(item=item,
                                   price=price,
                                   method=method,
                                   user=user)
        except Exception as e:
            logger.error(f'Не получилось записать данные в историю.\nОшибка: {e}'
                         f'\nКлиент: {user.pk}\nУслуга: {item.title}\nЦена: {price}\nМетод: {method}')
        return True
