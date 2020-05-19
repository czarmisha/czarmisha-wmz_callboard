from django.db import models
from django.urls import reverse


class Category(models.Model):
    image = models.ImageField(upload_to='images/', verbose_name='Фото')
    title = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"pk": self.pk})


class Ad(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    ad_type = models.ForeignKey('AdType', on_delete=models.CASCADE, verbose_name='Тип объявления')
    price = models.IntegerField(verbose_name='Цена')
    currency = models.ForeignKey('Currency', on_delete=models.CASCADE, verbose_name='Валюта')
    phone = models.IntegerField(verbose_name='Номер телефона')
    is_paid = models.BooleanField(default=False, verbose_name='Рекламировать')
    is_moderation = models.BooleanField(default=False, verbose_name='Модерация')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_archive = models.BooleanField(default=False, verbose_name='Архивное')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    # user = models.ForeignKey()
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город')
    district = models.ForeignKey('District', on_delete=models.CASCADE, verbose_name='Район', blank=True, null=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-pub_date']

    def __str__(self):
        return self.title


class AdType(models.Model):
    name = models.CharField(max_length=7, verbose_name='Название типа')

    class Meta:
        verbose_name = 'Тип объявления'
        verbose_name_plural = 'Типы объявления'

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=3, verbose_name='Название валюты')

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название города')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название района')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город района')

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'

    def __str__(self):
        return self.name
