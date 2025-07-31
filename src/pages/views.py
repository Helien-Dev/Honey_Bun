"""
Views for the 'pages' app.
This module contains view functions for rendering static pages in the application.
"""

from django.shortcuts import render
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
    return render(request, 'views/categories.html', {})

def offers_view(request):
    return render(request, 'views/offers.html', {})

def shop_view(request):
    return render(request, 'views/shops.html', {})
