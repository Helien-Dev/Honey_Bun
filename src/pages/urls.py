from django.urls import path

from .views import (
    home_view,
    search_view,
    categories_view,
    offers_view,
    shop_view,
)

urlpatterns = [
    path("", home_view, name="home"),
    path('search/', search_view, name='search'),
    path('categories/', categories_view, name='categories'),
    path('offers/', offers_view, name='offers'),
    path('shop/', offers_view, name='shop'),
]
