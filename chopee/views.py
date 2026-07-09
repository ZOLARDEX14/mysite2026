from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'chopee/home.html', {'products': products})

def product_create(request):
    return render(request, 'chopee/product/create.html')

def product_retrieve(request):
    return render(request, 'chopee/product/retrieve.html')

def product_update(request):
    return render(request, 'chopee/product/update.html')

def product_delete(request):
    return render(request, 'chopee/product/delete.html')
