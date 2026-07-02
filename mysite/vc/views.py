import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import Category, Product

# --- Existing Quiz API Views ---

def get_question(request):
    """
    GET /quiz/question
    Returns a predefined quiz question as JSON.
    """
    if request.method != 'GET':
        return HttpResponseBadRequest("Only GET method is allowed on this endpoint.")
        
    data = {
        "id": 1,
        "text": "ประเทศไทยมีกี่จังหวัด",
        "choices": [50, 68, 72, 77]
    }
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})

@csrf_exempt
def create_question(request):
    """
    POST /quiz/question/create
    Accepts and returns JSON representing a new quiz question.
    """
    if request.method != 'POST':
        return HttpResponseBadRequest("Only POST method is allowed on this endpoint.")
        
    try:
        # Load and parse JSON body
        if request.body:
            data = json.loads(request.body)
        else:
            # Fallback if no body is provided (for demo/default purposes)
            data = {
                "id": 9,
                "text": "ภาษาโปรแกรมใดได้รับความนิยมสูงสุดในวิทยาการข้อมูล",
                "choices": ["C", "C++", "C#", "Python", "R", "Julia"]
            }
            
        # Ensure json_dumps_params ensure_ascii=False to display Thai characters correctly
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON body.")

# --- Shopee E-commerce Views ---

def shop_home_view(request):
    """
    Renders the Shopee-like e-commerce shop page.
    Supports filtering by category, search query, and sorting.
    """
    # Fetch all categories for navigation
    categories = Category.objects.all()
    
    # Query parameters
    search_query = request.GET.get('q', '').strip()
    category_slug = request.GET.get('category', '').strip()
    sort_by = request.GET.get('sort', 'popular').strip()
    
    # Base queryset
    products = Product.objects.all()
    
    # Apply search filter
    if search_query:
        products = products.filter(name__icontains=search_query) | products.filter(description__icontains=search_query)
        
    # Apply category filter
    selected_category = None
    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=selected_category)
        
    # Apply sorting
    if sort_by == 'latest':
        products = products.order_by('-created_at')
    elif sort_by == 'top_sales':
        products = products.order_by('-sales_count')
    elif sort_by == 'price_asc':
        products = products.order_by('price')
    elif sort_by == 'price_desc':
        products = products.order_by('-price')
    else:  # 'popular'
        products = products.order_by('-rating', '-sales_count')
        
    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
        'search_query': search_query,
        'selected_sort': sort_by,
        'total_products_count': products.count(),
    }
    return render(request, 'shop.html', context)

def product_detail_api(request, product_id):
    """
    API view to return details of a single product as JSON (for AJAX dynamic modal).
    """
    product = get_object_or_404(Product, pk=product_id)
    data = {
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": float(product.price),
        "original_price": float(product.original_price) if product.original_price else None,
        "discount_percent": product.discount_percent,
        "image_url": product.image_url,
        "rating": float(product.rating),
        "sales_count": product.sales_count,
        "stock": product.stock,
        "location": product.location,
        "category": product.category.name,
    }
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
