from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('product/create', product_create),
    path('product/retrieve', product_retrieve),
    path('product/update', product_update),
    path('product/delete', product_delete),
]
