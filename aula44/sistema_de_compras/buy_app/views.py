from django.shortcuts import render
from django.http import HttpResponse
from .services import gerar_pix
from django.http import HttpRequest

# Create your views here.
def home(request):
    return render(request, 'index.html')

def comprar_pao(request):
    if request.method == 'POST':
        return processar_pagamento(request)
    return render(request, 'comprarPao.html')

def processar_pagamento(request):
    try:
        resultado_pix = gerar_pix(valor=0.50, descricao="Compra de produto")
        return render(request, 'pagamento.html', {
            'qr_code_path': resultado_pix['qr_code_image'],  # URL da imagem do QR code
            'qr_code_text': resultado_pix['qr_code'],        # Código PIX em texto
            'reference_id': resultado_pix['reference_id']     # ID da transação
        })
    except Exception as e:
        # Trate o erro adequadamente
        return HttpResponse(f"Erro ao gerar PIX: {str(e)}")
