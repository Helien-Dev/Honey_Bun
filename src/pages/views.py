"""
Views for the 'pages' app.
This module contains view functions for rendering static pages in the application.
"""

from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib.auth import get_user_model
from catalog.models import Product

User = get_user_model()

# Create your views here.
def home_view(request):
    """
    Renders the home page.
    """
    products = Product.objects.all().order_by('?')[:2]
    single_product = Product.objects.all().order_by('?')[:1]
    page = request.GET.get('page', 1)
    user = request.user

    context = {
        'title': 'Home',
        'description': 'description',
        'keywords': 'keywords',
        'og_title': 'og:title',
        'og_description': 'og:description',
        'og_type': 'og:type',
        'og_image': 'og:image',
        'user': user,
        'products': products,
        'single_product': single_product,
        'page': page,
    }

    return render(request, 'views/home.html', context)

def search_view(request):
    """
    Search view
    """
    context = {}

    if request.method == 'GET':
        searched = request.GET.get('searched', '')
        if not  searched:
            context['searched'] = searched
        else:
            products = Product.objects.filter(name__icontains=searched)
            context = {
                'searched': searched,
                'products': products,
            }

    return render(request, 'components/controls/search.html', context)

def categories_view(request):
    """
    Categories view
    """
    return render(request, 'views/categories.html', {})

def offers_view(request):
    """
    Offers view
    """
    return render(request, 'views/offers.html', {})

def shop_view(request):
    """
    Shop view
    """
    return render(request, 'views/shop.html', {})

def special_offers_view(request):
    """
    Special offers view
    """
    return render(request, 'views/special_offers.html', {})

def product_details_view(request, slug):
    """
    Product details view - Muestra los detalles de un producto específico
    """
    # Obtener el producto específico por slug o devolver 404 si no existe
    product = get_object_or_404(Product, slug=slug)

    # Obtener productos relacionados/recomendados (excluyendo el actual)
    recommended_products = Product.objects.exclude(slug=slug).order_by('?')[:4]

    user = request.user

    context = {
        'title': f'{product.name} - Detalles del Producto',
        'description': product.product_description[:160]
        if product.product_description else 'Detalles del producto',
        'keywords': f'{product.name}, producto, comprar',
        'og_title': product.name,
        'og_description': product.product_description[:160] if product.product_description else '',
        'og_type': 'product',
        'og_image': product.image_url,
        'user': user,
        'product': product,  # El producto principal
        'recommended_products': recommended_products,  # Productos recomendados
        'model_instance': recommended_products,  # Para el componente de recomendaciones
    }

    return render(request, 'views/product_details.html', context)

def profile_view(request):
    """
    Special offers view
    """
    
    context = {
        'title': 'Home',
        'description': 'description',
        'keywords': 'keywords',
        'og_title': 'og:title',
        'og_description': 'og:description',
        'og_type': 'og:type',
        'og_image': 'og:image',
    }
    
    return render(request, 'views/profile.html', {})
