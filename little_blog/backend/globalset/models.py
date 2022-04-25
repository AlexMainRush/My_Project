from django.db import models
from solo.models import SingletonModel


class GlobalSet(SingletonModel):
    logotype = models.ImageField(verbose_name='Логотип для сайта', null=True)
    document = models.FileField(verbose_name='Файл политики конфиденциальности')

    def __str__(self):
        return 'Глобальные элементы'

    class Meta:
        verbose_name = 'Глобальные настройки'
        verbose_name_plural = 'Глобальные настройки'