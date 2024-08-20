import logging
from django.core.exceptions import ObjectDoesNotExist
from .bitrix24Abstract import Bitrix24Abstract
from integrations.models import Services
from bitrix24 import Bitrix24

logger = logging.getLogger('site')


class Lead(Bitrix24Abstract):

    def __init__(self):
        self.hook = self.getHook()
        self.BitrixMethod = Bitrix24(self.hook)

    def update(self, id: int) -> bool:
        pass

    def add(self, user, data: dict) -> int:
        try:
            addLead = self.BitrixMethod.callMethod('crm.lead.add',
                                                   fields={
                                                       'STATUS_ID': 'NEW',
                                                       'NAME': user.first_name,
                                                       'PHONE': [{'VALUE': user.phone, 'VALUE_TYPE': 'WORK'}],
                                                       **data
                                                   })
            return addLead
        except Exception as e:
            logger.error(f'Сервис: Создание Лида в Битрикс24\nПри попытке создания лида произошла ошибка.\nОшибка: {e}'
                         f'\nКлиент: {user.pk}')
            raise ValueError('Произошла ошибка. Попробуйте позже')

    def get(self, id: int) -> bool:
        pass

    def getHook(self):
        try:
            hook = Services.objects.get(title='Bitrix24-Leads')
            return hook.hook
        except ObjectDoesNotExist as e:
            logger.critical(f'Хук Bitrix24 для лидов не найден.\nОшибка: {e}')
            raise ObjectDoesNotExist('Произошла ошибка. Попробуйте позже')
        except Exception as e:
            logger.critical(f'При попытке получить хук Bitrix24 для лидов появилась ошибка.\nОшибка: {e}')
            raise ObjectDoesNotExist('Произошла ошибка. Попробуйте позже')
