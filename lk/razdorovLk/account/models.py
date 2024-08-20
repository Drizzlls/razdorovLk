from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from currentStateOfAffairs.models import Affairs

class User(AbstractUser):
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=False)
    email = models.EmailField(_("email address"), unique=True)
    email_verify = models.BooleanField(default=False, verbose_name='Верификация Email')
    phone = models.IntegerField(verbose_name='Номер телефона', blank=True, null=True) # Номер телефона
    surname = models.CharField(max_length=25, verbose_name='Отчество', blank=True) # Отчество
    coins = models.PositiveIntegerField(verbose_name='Количество бонусов', blank=False, default=0)
    affair = models.ForeignKey(Affairs, on_delete=models.SET_NULL, null=True, verbose_name='Состояние дела', blank=True)
    idLeadFromBitrix24 = models.IntegerField(null=True, blank=True, verbose_name='ID лида из Битрикс24')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
