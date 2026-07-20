from django.shortcuts import render, redirect
from .models import Product

# 1. List / Read
def home(request):
    products = Product.objects.all()
    return render(request, 'chopee/home.html', {'products': products})

# 2. Create
def product_create(request):
    if request.method == 'POST':
        Product.objects.create(
            brand=request.POST['brand'],
            name=request.POST['name'],
            price=request.POST['price'],
            year=request.POST['year']
        )
        return redirect('/')
    return render(request, 'chopee/product/create.html')

# 3. Retrieve / Search
def product_retrieve(request):
    q = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=q) if q else None
    return render(request, 'chopee/product/retrieve.html', {'products': products})

# 4. Update
def product_update(request):
    pid = request.GET.get('id')
    product = Product.objects.filter(id=pid).first() if pid else None
    if request.method == 'POST':
        p = Product.objects.get(id=request.POST['id'])
        p.brand = request.POST['brand']
        p.name = request.POST['name']
        p.price = request.POST['price']
        p.year = request.POST['year']
        p.save()
        return redirect('/')
    return render(request, 'chopee/product/update.html', {'product': product})

# 5. Delete
def product_delete(request):
    pid = request.GET.get('id')
    if pid:
        Product.objects.filter(id=pid).delete()
        return redirect('/')
    return render(request, 'chopee/product/delete.html')
