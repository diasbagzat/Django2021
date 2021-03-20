from django.db import models


# Create your models here.

class TodoList(models.Model):
    task = models.CharField(max_length=255, null=True, blank=True, verbose_name='Задания')
    create_date = models.DateField(verbose_name='Дата Добавления')
    dueon_date = models.DateField(verbose_name='Дедлайн')
    owner = models.CharField(max_length=255, null=True, blank=True, verbose_name='Имя')
    mark = models.BooleanField(verbose_name='оценка')

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Список Задании'
        ordering =['create_date']




