from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Product

# 1. List
def home(request):
    products = Product.objects.all()
    return render(request, 'chopee/home.html', {'products': products})

# 2. Create
def product_create(request):
    if request.method == 'POST':
        brand = request.POST.get('brand', '').strip()
        name = request.POST.get('name', '').strip()
        price = request.POST.get('price', '0')
        year = request.POST.get('year', '2026')

        if brand and name:
            Product.objects.create(
                brand=brand,
                name=name,
                price=price,
                year=year
            )
        return redirect('/')

    return render(request, 'chopee/product/create.html')

# 3. Retrieve (Search)
def product_retrieve(request):
    q = request.GET.get('q', '').strip()
    products = None
    if q:
        products = Product.objects.filter(Q(brand__icontains=q) | Q(name__icontains=q))
    return render(request, 'chopee/product/retrieve.html', {'products': products, 'query': q})

# 4. Update
def product_update(request, pk=None):
    product_id = pk or request.GET.get('id') or request.POST.get('id')
    product = None
    if product_id:
        product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST' and product:
        product.brand = request.POST.get('brand', '').strip()
        product.name = request.POST.get('name', '').strip()
        product.price = request.POST.get('price', '0')
        product.year = request.POST.get('year', '2026')
        product.save()
        return redirect('/')

    return render(request, 'chopee/product/update.html', {'product': product})

# 5. Delete
def product_delete(request, pk=None):
    product_id = pk or request.GET.get('id') or request.POST.get('id')
    if product_id:
        product = get_object_or_404(Product, pk=product_id)
        product.delete()
        return redirect('/')

    return render(request, 'chopee/product/delete.html')
