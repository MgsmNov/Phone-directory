from django.core.validators import MinValueValidator
from django.db import models


# 1233215588
class Person(models.Model):
    surname = models.CharField(max_length=30, blank=False, verbose_name='Фамилия')
    name = models.CharField(max_length=30, blank=False, verbose_name='Имя')
    patronymic = models.CharField(max_length=30, blank=False, verbose_name='Отчество')
    organization_name = models.CharField(max_length=50, blank=False, verbose_name='Название организации')
    work_phone = models.DecimalField(max_digits=11, decimal_places=0, blank=False, verbose_name='Рабочий телефон',
                                     validators=[MinValueValidator(10000000000)])
    cell_phone = models.DecimalField(max_digits=11, decimal_places=0, blank=False, verbose_name='Сотовый телефон',
                                     validators=[MinValueValidator(10000000000)])

    def __str__(self):
        return (f"{self.surname} {self.name} {self.patronymic} {self.organization_name}"
                f" +{self.work_phone} +{self.cell_phone}")
