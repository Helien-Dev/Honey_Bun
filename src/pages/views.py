"""
Views for the 'pages' app.
This module contains view functions for rendering static pages in the application.
"""

from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
def home_view(request):
    """
    Renders the home page.
    """

    user = request.user

    context = {
        'title': 'Home',
        'description': 'description',
        'keywords': 'keywords',
        'og_title': 'og:title',
        'og_description': 'og:description',
        'og_type': 'og:type',
        'og_image': 'og:image',
        'user': user
    }

    return render(request, 'views/home.html', context)
