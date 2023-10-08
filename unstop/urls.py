from django.urls import path
from .views import book_tickets, reset_db

urlpatterns = [
    path('book-tickets/', book_tickets, name='book_tickets'),
    path('reset-db/', reset_db, name='reset_db'),
]
