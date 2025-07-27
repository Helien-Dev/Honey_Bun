"""
Views for the 'pages' app.
This module contains view functions for rendering static pages in the application.
"""

from django.shortcuts import render

# Create your views here.
def home_view(request):
    """
    Renders the home page.
    """
    return render(request, 'pages/home.html', {})
