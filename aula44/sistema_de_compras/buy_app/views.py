from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import logging

logger = logging.getLogger('buy_app')

# Create your views here.
def index(request):
    return render(request, 'index.html')

def comprar_pao(request):
    return render(request, 'comprarPao.html')

def processar_pagamento(request):
    return render(request, 'pagamento.html')
