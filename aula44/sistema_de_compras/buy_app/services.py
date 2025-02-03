import os
from gerencianet import Gerencianet
from django.conf import settings
import qrcode
import uuid
from datetime import datetime, timedelta

def get_gn_credentials():
    # Configurações base
    credentials = {
        'client_id': settings.GERENCIANET_CLIENT_ID,
        'client_secret': settings.GERENCIANET_CLIENT_SECRET,
        'sandbox': settings.GERENCIANET_SANDBOX,
        'pix_cert': settings.GERENCIANET_CERT_PATH,
        'base_url': 'api-pix.gerencianet.com.br'
    }

    # Verifica se o certificado existe
    if not os.path.exists(settings.GERENCIANET_CERT_PATH):
        raise Exception(f"Certificado não encontrado em: {settings.GERENCIANET_CERT_PATH}")

    return credentials

def gerar_pix(valor: float, descricao: str):
    try:
        # Inicializa a Gerencianet com as credenciais
        credentials = get_gn_credentials()
        gn = Gerencianet(credentials)
        
        # Body da requisição
        body = {
            "calendario": {
                "expiracao": 3600
            },
            "valor": {
                "original": f"{valor:.2f}"
            },
            "chave": settings.GERENCIANET_PIX_KEY,
            "solicitacaoPagador": descricao,
            "infoAdicionais": [
                {
                    "nome": "Pagamento",
                    "valor": "Compra de produto"
                }
            ]
        }

        # Criando cobrança
        response = gn.pix_create_immediate_charge(body=body)
        
        if 'loc' not in response:
            raise Exception(f"Resposta inesperada da API: {response}")
        
        # Gerando QR Code
        params = {
            "id": response["loc"]["id"]
        }
        qr_code_data = gn.pix_generate_qrcode(params=params)
        
        # Gerando imagem do QR code
        qr_code_path = gerar_qr_code(qr_code_data['qrcode'])
        
        return {
            'qr_code': qr_code_data['qrcode'],
            'qr_code_image': qr_code_path,
            'txid': response.get('txid', '')
        }
        
    except Exception as e:
        raise Exception(f"Erro ao criar cobrança PIX: {str(e)}")

def gerar_qr_code(qr_code_text):
    # Cria o diretório para os QR codes se não existir
    media_path = os.path.join(settings.BASE_DIR, 'media', 'qr_codes')
    os.makedirs(media_path, exist_ok=True)
    
    # Gera um nome único para o arquivo
    filename = f'qr_code_{uuid.uuid4()}.png'
    img_path = os.path.join(media_path, filename)
    
    # Gera o QR code
    img = qrcode.make(qr_code_text)
    img.save(img_path)
    
    # Retorna o caminho relativo para usar na URL
    return f'/media/qr_codes/{filename}'

def consultar_pix(txid):
    try:
        credentials = get_gn_credentials()
        gn = Gerencianet(credentials)
        
        params = {
            "txid": txid
        }
        response = gn.pix_detail_charge(params=params)
        return response
    except Exception as e:
        raise Exception(f"Erro ao consultar PIX: {str(e)}")