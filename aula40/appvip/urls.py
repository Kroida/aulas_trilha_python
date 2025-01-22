from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista-socios/', views.lista_socios, name='lista_socios'),
    path('delete-socios/', views.delete_socios, name='delete_socios'),
]
