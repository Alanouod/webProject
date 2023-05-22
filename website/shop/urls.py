from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('basket/', views.basket, name="basket"),
    path('order/', views.order, name="order"),
    path('update_item/', views.updateItem, name="updateItem"),
    
]