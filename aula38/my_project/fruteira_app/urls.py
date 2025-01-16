from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lista-frutas/', views.lista_frutas, name='lista_frutas'),
    path('cadastrar-fruta/', views.cadastrar_fruta, name='cadastrar_fruta'),
]
