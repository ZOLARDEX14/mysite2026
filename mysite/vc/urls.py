from django.urls import path
from . import views

urlpatterns = [
    path('question', views.get_question, name='get_question'),
    path('question/create', views.create_question, name='create_question'),
    path('api/products/<int:product_id>/', views.product_detail_api, name='product_detail_api'),
]
