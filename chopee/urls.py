from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/create', views.product_create, name='create'),
    path('product/retrieve', views.product_retrieve, name='retrieve'),
    
    path('product/update', views.product_update, name='update'),
    path('product/update/<int:pk>/', views.product_update, name='update_with_pk'),
    
    path('product/delete', views.product_delete, name='delete'),
    path('product/delete/<int:pk>/', views.product_delete, name='delete_with_pk'),
]
