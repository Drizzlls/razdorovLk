import logging
import requests


class TelegramBotHandler(logging.Handler):

    def emit(self, record):
        text = f'Проект: Личный кабинет\nВремя — {record.asctime}\nТип проблемы — {record.levelname}\nФункция — {record.filename}/{record.funcName}({record.lineno})\nПроблема — {record.message}'
        req = requests.get(f'https://api.telegram.org/bot7354303530:AAFXOhnoXVHLZZ038lH-pM9WZO9MosuKJeU/sendMessage?chat_id=272635960&text={text}')


