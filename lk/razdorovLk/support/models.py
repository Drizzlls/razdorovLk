import datetime

from django.db import models
from account.models import User

TOPIC_CHOICES = [
    ('complaint', 'Жалоба'),
    ('wish', 'Пожелание'),
]

class Support(models.Model):
    text = models.TextField(max_length=500,verbose_name='Текст заявки')
    user = models.ForeignKey(User, models.SET_NULL, null=True, verbose_name='Клиент')
    topic = models.CharField(max_length=15, choices=TOPIC_CHOICES, verbose_name='Тема')
    completed = models.BooleanField(default=False, verbose_name='Выполнено')
    comment = models.TextField(max_length=300, null=True, verbose_name='Комментарий', blank=True)
    dateCreate = models.DateField(auto_now_add=True, null=True, verbose_name='Дата создания')
    dateClose = models.DateField(verbose_name='Дата закрытия', blank=True, null=True)


    def __str__(self):
        return self.get_topic_display()

    class Meta:
        verbose_name = 'Жалобу'
        verbose_name_plural = 'Жалобы'

    def save(self,*args, **kwargs):
        if self.completed and not self.dateClose:
            self.dateClose = datetime.datetime.now()
        super().save(*args, **kwargs)



