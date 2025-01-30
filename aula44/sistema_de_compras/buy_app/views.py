from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def comprar_pao(request):
    return render(request, 'comprarPao.html')
