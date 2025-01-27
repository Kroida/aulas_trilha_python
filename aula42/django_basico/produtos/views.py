from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa

def ver_produto(request):
    if request.method == 'GET':
        nome = 'Luís'  
        return render(request, 'verProduto.html', {'nome': nome})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

        return HttpResponse("Produto inserido")

def inserir_produto(request):
    return HttpResponse("Produto inserido")
