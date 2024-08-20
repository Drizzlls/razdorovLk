import requests
import logging

logger = logging.getLogger('site')

class TelegramBot:
    """  Отправка данных в ТГ бот """
    SERVICE_NAME = {
        'support' : 'Поддержка'
    }

    API_TOKEN = 'bot7354303530:AAFXOhnoXVHLZZ038lH-pM9WZO9MosuKJeU'

    def sendMessageFromService(self, service: str, text: str, id: int) -> bool:
        """
        :param service: Название сервиса
        :param text: Текст сообщения
        :param id: ID заявки
        :return: True
        """
        textFromService = f'Личный кабинет\nCервис: {self.SERVICE_NAME.get(service,service)}\nПоступило новое сообщение в поддержку:\n{text}\nID заявки: {id}'
        try:
            req = requests.get(f'https://api.telegram.org/404{self.API_TOKEN}/sendMessage?chat_id=272635960&text={textFromService}')
            if req.status_code != 200:
                logger.error(f'Сервис: Отправка данных в тг об ошибках\nСтатуc: {req.status_code}\nТекст: {req.text}')
        except Exception as e:
            logger.critical(f'Сервис: Отправка данных в тг об ошибках\nОшибка: {e}')
        return True

