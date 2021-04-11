from django.urls import path
from .views import wish_shakti

urlpatterns = [
    path('', wish_shakti, name='wish_shakti'),
]
