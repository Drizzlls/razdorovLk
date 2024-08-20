from django.db import models


class Services(models.Model):
    title = models.CharField(max_length=50, null=False, verbose_name='Название сервиса')
    hook = models.CharField(max_length=100, null=False, verbose_name='Хук')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'