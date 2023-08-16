from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='продукт')
    description = models.TextField(verbose_name='описание')
    image_preview = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.CharField(max_length=100, verbose_name='категория')
    purchase_price = models.IntegerField(verbose_name='цена')
    created_date = models.DateTimeField(verbose_name='создан')
    modified_date = models.DateTimeField(verbose_name='изменен')

    in_stock = models.BooleanField(default=True, verbose_name='есть в наличии')

    def __str__(self):
        return f'Product: {self.product_name}'

    class Meta:
        verbose_name = 'продукт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты'  # Настройка для наименования набора объектов
        ordering = ('purchase_price',)


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='категория')
    description = models.TextField(verbose_name='описание')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='создан')

    def __str__(self):
        return f'Category: {self.category_name}'

    class Meta:
        verbose_name = 'категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'  # Настройка для наименования набора объектов
        ordering = ('category_name',)
