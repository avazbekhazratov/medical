from django.urls import path
from app.views import index, get_xamshira, get_doktor, get_xona, get_bemor

urlpatterns = [
    path('', index, name='home'),
    path('get_doktor/', get_doktor, name='get_doktor'),
    path('get_xona/', get_xona, name='get_xona'),
    path('get_bemor/', get_bemor, name='get_bemor'),
    path('get_bemor/<int:pk>/', get_bemor, name='get_bemor'),
    path('get_xamshira/', get_xamshira, name='get_xamshira'),
]
