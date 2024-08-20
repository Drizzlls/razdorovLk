import logging
from typing import Dict, Any

from integrations.models import Services
from bitrix24 import Bitrix24
from django.core.exceptions import ObjectDoesNotExist

logger = logging.getLogger('site')


class EmployeeFromBitrix24:
    """ Работа с сотрудниками из Битрикс24 """
    def __init__(self):
        self.hook = self.getHook()
        self.BitrixMethod = Bitrix24(self.hook)

    def get(self, id:str) -> dict[str, Any] | None:
        """ Получить сотрудника """
        print('Получаю сотрудника из битрикса')
        try:
            employee = self.BitrixMethod.callMethod('user.get', {'ID': id})
            if employee:
                return employee
            else:
                return None
        except Exception as e:
            logger.error(f'При попытке получить сотрудника из Bitrix24 появилась ошибка.\nОшибка: {e}')
            return None


    def getHook(self):
        try:
            hook = Services.objects.get(title='Bitrix24-Employee')
            return hook.hook
        except ObjectDoesNotExist as e:
            logger.critical(f'Хук Bitrix24 для сотрудников не найден.\nОшибка: {e}')
            raise ObjectDoesNotExist('Произошла ошибка. Попробуйте позже')
        except Exception as e:
            logger.critical(f'При попытке получить хук Bitrix24 для сотрудников появилась ошибка.\nОшибка: {e}')
            raise ObjectDoesNotExist('Произошла ошибка. Попробуйте позже')
