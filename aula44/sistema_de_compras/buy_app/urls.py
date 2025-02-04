from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('comprar_pao/', views.comprar_pao, name='comprar_pao'),
    path('processar_pagamento/', views.processar_pagamento, name='processar_pagamento')
]