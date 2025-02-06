from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def comprar_pao(request):
    return render(request, 'comprarPao.html')

def processar_pagamento(request):
    return render(request, 'pagamento.html')
