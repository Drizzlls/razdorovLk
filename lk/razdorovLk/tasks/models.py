from django.db import models

class Tasks(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название задачи')
    description = models.CharField(max_length=150, verbose_name='Краткое описание задачи')
    coins = models.IntegerField(verbose_name='Количество баллов')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задачу'
        verbose_name_plural = 'Задачи'
