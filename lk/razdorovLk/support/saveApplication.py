import logging

from .models import Support
from integrations.telegram.telegramAPI import TelegramBot
logger = logging.getLogger('site')

class Application(TelegramBot):

    def saveApplication(self, userform, request):
        form = userform.save(commit=False)
        try:
            form.user = request.user
            form.save()
        except Exception as e:
            logger.error(f'Сервис: Обращение в поддержку\nОшибка создания заявки\nКлиент: {request.user.pk}\n'
                         f'Текст заявки: {form.text}\nОшибка: {e}')
        self.sendMessageFromService(service='support', text=form.text, id=form.pk)