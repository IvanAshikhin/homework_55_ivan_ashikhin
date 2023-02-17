from django.db import models


# Create your models here.

class Article(models.Model):
    description = models.TextField(max_length=500, null=False, blank=False, verbose_name='Описание задачи')
    status = models.CharField(max_length=100, null=False, default='new', blank=False, verbose_name='Статус')
    done_date = models.DateField(auto_now=False, verbose_name="Дата выполнения")

    def __str__(self):
        return f'{self.description} {self.status} {self.done_date}'
