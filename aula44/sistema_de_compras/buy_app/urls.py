from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('comprar_pao/', views.comprar_pao, name='comprar_pao')
]