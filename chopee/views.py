from django.shortcuts import render, redirect
from .models import Product, Category

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'chopee/home.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        brand = request.POST.get('brand', '').strip()
        name = request.POST.get('name', '').strip()
        price = request.POST.get('price', '0')
        year = request.POST.get('year', '2026')

        if brand and name:
            # Find or create category based on brand name
            category, created = Category.objects.get_or_create(name=brand)
            
            # Create product
            Product.objects.create(
                name=name,
                price=price,
                year=year,
                category=category,
                description=f"Brand: {brand}, Year: {year}"
            )
        return redirect('/')

    return render(request, 'chopee/product/create.html')

def product_retrieve(request):
    return render(request, 'chopee/product/retrieve.html')

def product_update(request):
    return render(request, 'chopee/product/update.html')

def product_delete(request):
    return render(request, 'chopee/product/delete.html')
