from django.urls import path

from .views import (
    home_view,
    search_view,
    categories_view,
    offers_view,
    shop_view,
    special_offers_view,
    product_details_view,
)

urlpatterns = [
    path("", home_view, name="home"),
    path('search/', search_view, name='search'),
    path('categories/', categories_view, name='categories'),
    path('offers/', offers_view, name='offers'),
    path('special_offers/', special_offers_view, name='special_offers'),
    # path('product_details/', product_details_view, name='product_details'),
    path('product/<slug:slug>/', product_details_view, name='product_details'),
    path('shop/', shop_view, name='shop'),
]
