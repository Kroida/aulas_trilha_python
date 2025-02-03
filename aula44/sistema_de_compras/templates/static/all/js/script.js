function copyToClipboard() {
    const textarea = document.querySelector('textarea');
    textarea.select();
    document.execCommand('copy');
    alert('Código PIX copiado!');
}

// Atualiza o status do pagamento a cada 5 segundos
function checkPaymentStatus() {
    const txid = document.querySelector('p').textContent.split(': ')[1];
    
    fetch(`/verificar_pagamento/${txid}/`)
        .then(response => response.json())
        .then(data => {
            if (data.status === 'CONCLUIDA') {
                alert('Pagamento recebido com sucesso!');
                window.location.href = '/';  // Redireciona para a página inicial
            }
        })
        .catch(error => console.error('Erro:', error));
}

// Inicia a verificação do status
setInterval(checkPaymentStatus, 5000);
