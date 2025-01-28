from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ver_produto(request):
    if request.method == 'GET':
        nome = request.GET['nome']
        return render(request, 'ver_produto.html', {'nome': nome})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

        pessoa = Pessoa(nome=nome, idade=idade)
        pessoa.save()

        return HttpResponse('Dados cadastrados com sucesso!')
    

def inserir_produto(request):
    return HttpResponse(f'Estou no inserir produto')