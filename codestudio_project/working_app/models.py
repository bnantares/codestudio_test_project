from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.html import format_html
from django.utils.functional import cached_property
from django_resized import ResizedImageField
from django.shortcuts import reverse
import uuid
import os

def get_image_path(instance, img_name):
    img_name = img_name.split('.')[0]
    img_dir = 'img_dir/working_app/'
    img_extension = 'jpg'
    img_name = '%s.%s' % (uuid.uuid4(), img_extension)

class HomePage(models.Model):
    '''Создадим модель для главной страницы'''
    title = models.CharField(
        'Заголовок', max_length=255, help_text='Обязательное поле'
    )
    keywords = models.CharField(
        'Ключевые слова', max_length=255, blank=True
    )
    description = models.TextField(
        'Описание', blank=True
    )
    slide_photo_heading_text = models.CharField(
        'Заголовок над слайдером', max_length=255, blank=True
    )
    slide_photo_bottom_text = models.TextField(
        'Текст под слайдером', blank=True
    )
    product_heading_text = models.CharField(
        'Заголовок продуктов', max_length=255, blank=True
    )
    map_latitude = models.DecimalField(
        'Широта', max_digits=5, decimal_places=2
    )
    map_longitude = models.DecimalField(
        'Долгота', max_digits=5, decimal_places=2
    )
    feedback_form_title = models.CharField(
        'Заголовок формы фидбека', max_length=255, blank=True
    )

    class Meta:
        verbose_name = "данные"
        verbose_name_plural = "Главная страница"

    def __str__(self):
        return self.title


class HomePageImage(models.Model):
    '''Создадим модель для добавления картинок в слайдер на главной странице'''
    homepage = models.ForeignKey(
        HomePage, on_delete=models.CASCADE, blank=True, verbose_name='Картинка для слайдера',
        related_name='homepage_image'
    )
    image = ResizedImageField(
        'Фото для слайдера', size=[1280, 860], crop=['middle', 'center'],
        quality=80,
        upload_to='images/', validators=[FileExtensionValidator(['jpg', 'jpeg'])],
        help_text='Допускаются только изображения в формате .jpg, .jpeg'
    )
    @cached_property  # иначе картинка при изменении будет отображаться старая
    def display_image(self):
        return format_html('<img src="{img}" width="300">', img=self.image.url)
    display_image.short_description = 'Предпросмотр изображения'

    class Meta:
        verbose_name = "слайд"
        verbose_name_plural = "слайды"

    def __str__(self):
        return 'элемент'

class Product(models.Model):
    title = models.CharField(
        'Заголовок', max_length=255, help_text='Обязательное поле'
    )
    keywords = models.CharField(
        'Ключевые слова', max_length=255, blank=True
    )
    description = models.TextField(
        'Описание', blank=True
    )
    name = models.CharField(
        'Название продукта', max_length=255, help_text='Обязательное поле'
    )
    date_pub = models.DateTimeField(
        auto_now_add=True
    )
    slug = models.SlugField(
        'URL', max_length=255, unique=True, null=True
    )
    image = ResizedImageField(
        'Фото продукта', size=[1280, 860], crop=['middle', 'center'],
        quality=80,
        upload_to='images/', validators=[FileExtensionValidator(['jpg', 'jpeg'])],
        help_text='Допускаются только изображения в формате .jpg, .jpeg',
        blank=True, null=True
    )
    heading1 = models.CharField(
        'Заголовок продукта 1', max_length=255,
        blank=True
    )
    heading2 = models.CharField(
        'Заголовок продукта 2', max_length=255,
        blank=True
    )
    heading3 = models.CharField(
        'Заголовок продукта 3', max_length=255,
        blank=True
    )
    text1 = models.TextField(
        'Содержание пункта 1', blank=True
    )
    text2 = models.TextField(
        'Содержание пункта 2', blank=True
    )
    text3 = models.TextField(
        'Содержание пункта 3', blank=True
    ) 
    @cached_property  # иначе картинка при изменении будет отображаться старая
    def display_image(self):
        return format_html('<img src="{img}" width="300">', img=self.image.url)
    display_image.short_description = 'Предпросмотр изображения'

    def get_absolute_url(self):
        '''Получим ссылку на страницу с уникальным URL'''
        return reverse('product_detail_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ['-date_pub']

    def __str__(self):
        return self.name