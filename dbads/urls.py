from django.urls import path, include
from .views import dbadspage


urlpatterns = [
    path('', dbadspage, name='dbadspage'),
]