from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Fruta
from decimal import Decimal
from django.db import IntegrityError

# Create your views here.

def home(request):
    return render(request, 'my_app/home.html')

def lista_frutas(request):
    # TODO: Buscar frutas do banco de dados
    frutas = Fruta.objects.all().order_by('nome')
    return render(request, 'my_app/lista_de_frutas.html', {'frutas': frutas})

def cadastrar_fruta(request):
    if request.method == 'POST':
        try:
            nome = request.POST.get('nome')
            preco = request.POST.get('preco')
            quantidade = request.POST.get('quantidade')
            
            # Validações básicas
            if not nome or not preco or not quantidade:
                messages.error(request, 'Todos os campos são obrigatórios.')
                return render(request, 'my_app/cadastrar_fruta.html')
            
            # Converter valores
            try:
                preco = Decimal(preco)
                quantidade = int(quantidade)
            except (ValueError, TypeError):
                messages.error(request, 'Valores inválidos para preço ou quantidade.')
                return render(request, 'my_app/cadastrar_fruta.html')
            
            # Verificar se já existe uma fruta com o mesmo nome
            if Fruta.objects.filter(nome=nome).exists():
                messages.error(request, f'Já existe uma fruta cadastrada com o nome {nome}.')
                return render(request, 'my_app/cadastrar_fruta.html')
            
            # Criar nova fruta
            fruta = Fruta.objects.create(
                nome=nome,
                preco=preco,
                quantidade=quantidade
            )
            
            messages.success(request, f'Fruta {fruta.nome} cadastrada com sucesso!')
            return redirect('lista_frutas')
        except Exception as e:
            messages.error(request, f'Erro ao cadastrar fruta: {str(e)}')
            return render(request, 'my_app/cadastrar_fruta.html')
            
    return render(request, 'my_app/cadastrar_fruta.html')
