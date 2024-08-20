import logging
from typing import Dict, Any
from django.core.exceptions import ObjectDoesNotExist
from .bitrix24Abstract import Bitrix24Abstract
from integrations.models import Services
from bitrix24 import Bitrix24

logger = logging.getLogger('site')


class Deal(Bitrix24Abstract):

    def __init__(self):
        self.hook = self.getHook()
        self.BitrixMethod = Bitrix24(self.hook)

    def update(self, id: int) -> bool:
        pass

    def add(self):
        pass

    def get(self, id: int) -> dict[str, Any] | bool:
        try:
            getLead = self.BitrixMethod.callMethod('crm.deal.get', ID=id)
            return getLead
        except Exception as e:
            logger.critical(f"При попытке получить сделку в Bitrix24 произошла ошибка.\nОшибка: {e}")
            return False

    def getHook(self):
        try:
            hook = Services.objects.get(title='Bitrix24-Deals')
            return hook.hook
        except ObjectDoesNotExist as e:
            logger.critical(f'Хук Bitrix24 для сделок не найден.\nОшибка: {e}')
            raise ObjectDoesNotExist('Произошла ошибка. Попробуйте позже')
        except Exception as e:
            logger.critical(f'При попытке получить хук Bitrix24 для сделок появилась ошибка.\nОшибка: {e}')
            raise ObjectDoesNotExist('Произошла ошибка. Попробуйте позже')
