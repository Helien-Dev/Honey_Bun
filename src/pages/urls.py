from django.urls import path
from .views import home_view
import widgets

urlpatterns = [
    path("", home_view, name="home"),
]
