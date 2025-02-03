from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpRequest
from .services import gerar_pix, consultar_pix

# Create your views here.
def index(request):
    return render(request, 'index.html')

def comprar_pao(request):
    return render(request, 'comprarPao.html')

def processar_pagamento(request):
    try:
        resultado_pix = gerar_pix(valor=0.10, descricao="Compra de produto")
        return render(request, 'pagamento.html', {
            'qr_code_path': resultado_pix['qr_code_image'],
            'qr_code_text': resultado_pix['qr_code'],
            'txid': resultado_pix['txid']
        })
    except Exception as e:
        return HttpResponse(f"Erro ao gerar PIX: {str(e)}")

def verificar_pagamento(request, txid):
    try:
        status = consultar_pix(txid)
        return JsonResponse(status)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
