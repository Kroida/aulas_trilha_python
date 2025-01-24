from django.shortcuts import render
from django.http import HttpResponse

def ver_produto(request):
    nome = 'Luis'   
    return render(request, 'verProduto.html', {'nome': nome})

def inserir_produto(request):
    return HttpResponse("Produto inserido")
