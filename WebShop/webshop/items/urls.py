from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('ajax_cart', ajax_cart),
    path('ajax_cart_display', ajax_cart_display),
    path('ajax_del_item', ajax_del_item)
]
