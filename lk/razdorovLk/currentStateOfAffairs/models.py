from django.db import models


class StageAffairs(models.Model):
    """ Стадии """
    title = models.CharField(max_length=100, verbose_name='Название стадии', null=False)
    description = models.TextField(max_length=300, verbose_name='Описании стадии', null=False)
    video = models.CharField(max_length=150, verbose_name='ID видео из Youtube', null=True, blank=True)
    slug = models.SlugField(null=False, unique=True)
    stageId = models.CharField(max_length=15, verbose_name='ID стадии', null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Стадию'
        verbose_name_plural = 'Стадии'


class Employees(models.Model):
    """ Сотрудники """
    name = models.CharField(max_length=50, verbose_name='Имя')
    lastName = models.CharField(max_length=50, verbose_name='Фамилия')
    secondName = models.CharField(max_length=50, verbose_name='Отчество')
    personalId = models.CharField(max_length=30, verbose_name='Личный ID', unique=True)
    phone = models.CharField(max_length=20, verbose_name='Телефон')

    def __str__(self):
        return f'{self.name} {self.lastName}'

    class Meta:
        verbose_name = 'Сотрудника'
        verbose_name_plural = 'Сотрудники'


class Affairs(models.Model):
    stage = models.ForeignKey(StageAffairs, on_delete=models.SET_NULL, null=True,
                              verbose_name='Текущая стадия')  # UF_CRM_62DAB2BE1B9C0
    dateOfConclusion = models.DateField(null=True, verbose_name='Дата заключения сделки', blank=True)  # UF_CRM_62DAB2BE1B9C0
    depositPaymentDate = models.DateField(null=True, verbose_name='Дата оплаты депозита', blank=True)  # UF_CRM_1671619988
    manager = models.ForeignKey(Employees, on_delete=models.SET_NULL, null=True,
                                verbose_name='Менеджер по продажам', related_name='manager')  # ASSIGNED_BY_ID
    support = models.ForeignKey(Employees, on_delete=models.SET_NULL, null=True,
                                verbose_name='Менеджер поддержки', related_name='support')
    boss = models.ForeignKey(Employees, on_delete=models.SET_NULL, null=True,
                             verbose_name='Руководитель', related_name='boss')
    dateOfSendingToCourt = models.DateField(null=True, verbose_name='Дата отправки в суд', blank=True)  # UF_CRM_1676966915519
    caseNumber = models.CharField(max_length=100, null=True, verbose_name='Номер дела', blank=True)  # UF_CRM_6059A855ED8BE
    dateOfBankruptcy = models.DateField(null=True, verbose_name='Дата признания банкротом', blank=True)  # UF_CRM_1674476382
    completionDate = models.DateField(null=True, verbose_name='Дата завершения', blank=True)  # UF_CRM_1560238657391
    idDeal = models.IntegerField(verbose_name='ID сделки', unique=True, null=True, blank=True) # ID
    linkToKadArbitr = models.URLField(max_length=200, verbose_name='Ссылка на КадАрбитр', null=True, blank=True) # UF_CRM_1686001000739

    class Meta:
        verbose_name = 'Дела'
        verbose_name_plural = 'Дела'

    def __str__(self):
        return f'{self.idDeal}'
