from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index_url'),
    path('<str:slug>/', get_product, name='product_detail_url'),
]