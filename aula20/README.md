# 🃏 Baralho Mágico – Sequência da Montanha Sagrada

## Objetivo
Simular um baralho de cartas mágicas, onde cada carta representa uma lição de autoconhecimento. O usuário pode sortear cartas, visualizar cartas sorteadas, ler descrições e embaralhar o baralho.

---

## Funcionalidades Principais

- **1. Tirar carta:** Sorteia uma carta aleatória do baralho e a move para a pilha de cartas sorteadas.
- **2. Mostrar baralho:** Exibe todas as cartas já sorteadas.
- **3. Exibir descrição:** Mostra a descrição detalhada de uma carta sorteada escolhida pelo usuário.
- **4. Embaralhar baralho:** Retorna todas as cartas sorteadas ao baralho, embaralha e reinicia o jogo.
- **5. Sair:** Encerra o programa.

---

## Estrutura do Código

- **Dicionário `baralho`:** Armazena as cartas e suas descrições.
- **Dicionário `baralho_sorteado`:** Guarda as cartas já sorteadas.
- **Funções:** Cada opção do menu é uma função separada, facilitando a leitura e manutenção.
- **Loop principal:** Exibe o menu e executa as ações conforme a escolha do usuário.

---

## Fluxo Visual

```
[Menu Principal]
	↓
[Escolha do Usuário]
	↓
┌─────────────┬──────────────┬───────────────┬──────────────┬─────────────┐
│ Tirar Carta│ Mostrar Cartas│ Exibir Info  │ Embaralhar  │   Sair      │
└─────────────┴──────────────┴───────────────┴──────────────┴─────────────┘
```

---

## Destaques

- Uso de dicionários para manipular cartas.
- Funções bem separadas para cada ação.
- Mensagens claras para o usuário.
- Fácil de expandir com novas cartas ou funcionalidades.

---
