from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('product/create', views.product_create),
    path('product/retrieve', views.product_retrieve),
    path('product/update', views.product_update),
    path('product/delete', views.product_delete),
]
