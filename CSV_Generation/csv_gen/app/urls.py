from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('main', data_schemas),
    path('new_schemas', new_schemas),
    path('checkbox', ajax_form),
    path('ajax_form', ajax_form),

]