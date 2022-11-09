
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.quotation, name='quotation'),
    path('painting/', views.painting, name='painting'),
    
]

