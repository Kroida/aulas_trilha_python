import uuid
import requests
import qrcode
import os
from django.conf import settings


import uuid
import requests
import os
from datetime import datetime, timedelta
from django.conf import settings


def gerar_pix(valor: float, descricao: str):
    url = f"{settings.PAGBANK_API_URL}/orders"
    
    # Converte o valor para centavos (API espera o valor em centavos)
    valor_em_centavos = int(valor * 100)
    
    # Gera um ID único para a transação
    reference_id = str(uuid.uuid4())
    
    # Gera data de expiração (1 hora no futuro)
    expiration_date = (datetime.now() + timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%S-03:00")
    
    headers = {
        'Authorization': f'Bearer {settings.PAGBANK_TOKEN}',
        'Content-Type': 'application/json'
    }
    
    data = {
        "reference_id": reference_id,
        "customer": {
            "name": "Comprador Teste",
            "email": "comprador@teste.com",
            "tax_id": "12345678909"
        },
        "items": [
            {
                "reference_id": "item-1",
                "name": descricao,
                "quantity": 1,
                "unit_amount": valor_em_centavos
            }
        ],
        "qr_codes": [
            {
                "amount": {
                    "value": valor_em_centavos
                },
                "expiration_date": expiration_date
            }
        ],
        "shipping": {
            "address": {
                "street": "Avenida Brigadeiro Faria Lima",
                "number": "1384",
                "complement": "4 andar",
                "locality": "Pinheiros",
                "city": "São Paulo",
                "region": "São Paulo",
                "region_code": "SP",
                "country": "BRA",
                "postal_code": "01452002"
            }
        },
        "notification_urls": [
            "https://meusite.com/notificacoes"
        ]
    }

    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code in [200, 201]:
        order_data = response.json()
        qr_code = order_data.get('qr_codes', [{}])[0]
        return {
            'qr_code': qr_code.get('text'),
            'qr_code_image': qr_code.get('links', [{}])[0].get('href'),
            'reference_id': reference_id
        }
    else:
        raise Exception(f"Erro ao criar o pagamento PIX: {response.text}")


def gerar_qr_code(url_pix):
    # Cria o diretório para os QR codes se não existir
    media_path = os.path.join(settings.BASE_DIR, 'media', 'qr_codes')
    os.makedirs(media_path, exist_ok=True)
    
    # Gera um nome único para o arquivo
    filename = f'qr_code_{uuid.uuid4()}.png'
    img_path = os.path.join(media_path, filename)
    
    # Gera o QR code
    img = qrcode.make(url_pix)
    img.save(img_path)
    
    # Retorna o caminho relativo para usar na URL
    return f'/media/qr_codes/{filename}'