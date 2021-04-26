from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.utils.safestring import mark_safe
from PIL import Image
from django.forms import ModelForm, ValidationError
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget 
from django import forms

MAX_IMAGE_SIZE = 2048*1024

class ProductAdminForm(ModelForm):
    '''Используем CKEditor для добавления любого кол-ва пунктов в продукты'''
    text1 = forms.CharField(widget=CKEditorUploadingWidget(), label='Параграфы продукта 1', required = False)
    text2 = forms.CharField(widget=CKEditorUploadingWidget(), label='Параграфы продукта 2', required = False)
    text3 = forms.CharField(widget=CKEditorUploadingWidget(), label='Параграфы продукта 3', required = False)

    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            f'<span style="color:blue;">Загружайте изображеня не более 2МБ</span>'            
        )

    def clean_image(self):   
        image = self.cleaned_data['image']
        img = Image.open(image)
        if image.size > MAX_IMAGE_SIZE:
            raise ValidationError('Размер изображения не должен превышать 2MB')
        return image

    class Meta:
        model = Product
        fields = '__all__'

class HomePageImageAdminForm(ModelForm):

    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            f'<span style="color:blue;">Загружайте изображеня не более 2МБ</span>'            
        )

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        if image.size > MAX_IMAGE_SIZE:
            raise ValidationError('Размер изображения не должен превышать 2MB')
        return image


class HomePageImageAdminInLine(admin.StackedInline):
    '''Добавим возможность загрузить фото (с предпросмотром - display_image)'''
    model = HomePageImage
    form = HomePageImageAdminForm
    fields = [
        'image',
        'display_image',
    ]
    extra = 0
    classes = ('wide', )
    readonly_fields = ('display_image', )

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    '''Добавим возможность загрузить изображения'''
    inlines = [
        HomePageImageAdminInLine,
    ]

    fieldsets = (
        ("Блок SEO", {
            'fields': ('title', 'keywords', 'description'),
            'classes': ('collapse',),
        }),
        ("Контент", {
            'fields': (
                'slide_photo_heading_text',
                'slide_photo_bottom_text',
                'product_heading_text',
                'map_latitude', 'map_longitude',
                'feedback_form_title',
            ),
        }),
    )


    '''Для удобства (кнопка "сохранить" будет еще и наверху)'''
    save_on_top = True

    '''Уберем возможность добавлять...'''
    def has_add_permission(self, request, obj=None):
        return False

    '''...и удалять новые модели главной страницы'''
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    fieldsets = (
        ("Блок SEO", {
            'fields': ('title', 'keywords', 'description', 'slug'),
            'classes': ('collapse',),
        }),
        ("Контент", {
            'fields': (
                'name',
                'image', 'display_image',
                'heading1', 'text1',
                'heading2', 'text2',
                'heading3', 'text3',
                'date_pub',
            ),
        }),
    )
    readonly_fields = ('display_image', 'date_pub')

    save_on_top = True

'''Уберем ненужные нам элементы, отредактикуем заголовок админки'''
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.site_header = 'Управление контентом'


