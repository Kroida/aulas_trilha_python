from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Socio

# Create your views here.
def index(request):
    if request.method == 'POST':
        try:
            Socio.objects.create(
                nome_completo=request.POST['nome_completo'],
                cpf=request.POST['cpf'],
                email=request.POST['email'],
                telefone=request.POST['telefone'],
                data_nascimento=request.POST['data_nascimento'],
                tipo_socio=request.POST['tipo_socio'],
                mensagem=request.POST['mensagem']
            )
            messages.success(request, 'Sócio cadastrado com sucesso!')
            return redirect('index')
        except Exception as e:
            messages.error(request, 'Erro ao cadastrar sócio. Por favor, tente novamente.')
    
    return render(request, 'appvip/index.html')

def lista_socios(request):
    socios = Socio.objects.all().order_by('-data_cadastro')
    return render(request, 'appvip/lista_socios.html', {'socios': socios})

def delete_socios(request):
    if request.method == 'POST':
        socio_ids = request.POST.getlist('socios[]')
        try:
            Socio.objects.filter(id__in=socio_ids).delete()
            messages.success(request, 'Sócios selecionados foram excluídos com sucesso!')
        except Exception as e:
            messages.error(request, 'Erro ao excluir sócios. Por favor, tente novamente.')
    
    return redirect('lista_socios')