# Generated by Django 3.2 on 2021-04-24 11:43

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('working_app', '0002_auto_20210424_1421'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepageimage',
            options={'verbose_name': 'слайд', 'verbose_name_plural': 'слайды'},
        ),
        migrations.AlterField(
            model_name='homepageimage',
            name='homepage',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='homepage_image', to='working_app.homepage', verbose_name='Картинка для слайдера'),
        ),
        migrations.AlterField(
            model_name='homepageimage',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format=None, keep_meta=True, quality=0, size=[1280, 860], upload_to='images/', verbose_name='Фото для слайдера'),
        ),
    ]
