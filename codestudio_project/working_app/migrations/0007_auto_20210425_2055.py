# Generated by Django 3.2 on 2021-04-25 17:55

import django.core.validators
from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('working_app', '0006_auto_20210424_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='heading1',
            field=models.CharField(blank=True, max_length=255, verbose_name='Заголовок продукта 1'),
        ),
        migrations.AlterField(
            model_name='product',
            name='heading2',
            field=models.CharField(blank=True, max_length=255, verbose_name='Заголовок продукта 2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='heading3',
            field=models.CharField(blank=True, max_length=255, verbose_name='Заголовок продукта 3'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, help_text='Допускаются только изображения в формате .jpg, .jpeg', keep_meta=True, null=True, quality=80, size=[1280, 860], upload_to='images/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg'])], verbose_name='Фото продукта'),
        ),
    ]
