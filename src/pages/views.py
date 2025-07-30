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
    context = { }

    return render(request, 'pages/home.html', context)
