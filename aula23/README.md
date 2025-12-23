# Jogo de Dados – General Simplificado

Este projeto implementa um jogo de dados inspirado no clássico "General" (ou "Yahtzee"), utilizando Python puro e execução via terminal.

## Descrição Geral
O arquivo `general.py` contém toda a lógica do jogo, permitindo ao usuário jogar rodadas, guardar dados, visualizar pontuações e encerrar o programa. O objetivo é obter combinações especiais de dados para marcar pontos em cada rodada.

## Como Jogar
1. **Execute o arquivo**:
   ```bash
   python general.py
   ```
2. **Menu Principal:**
   - **1. Jogar dados:** Lança os dados e permite escolher quais guardar.
   - **2. Ver dados guardados:** Mostra os dados já guardados na rodada atual.
   - **3. Ver pontuação das rodadas:** Exibe a pontuação acumulada de cada rodada.
   - **4. Sair:** Encerra o programa.

3. **Regras de Pontuação:**
   - **Sequência Baixa (S):** 1-2-3-4-5 ou 2-3-4-5-6 (20 pontos)
   - **Full House (F):** 3 dados de um valor + 2 de outro (30 pontos)
   - **Quadra (P):** 4 dados iguais (40 pontos)
   - **General (G):** 5 dados iguais (50 pontos)

4. **Rodadas:**
   - Cada rodada permite até 3 tentativas para lançar e guardar dados.
   - Após as tentativas, a pontuação é calculada e registrada.

## Estrutura do Código
- **Funções principais:**
  - `menu()`: Exibe o menu de opções.
  - `jogar_dados()`: Lança os dados e permite guardar.
  - `ver_dados()`: Mostra dados guardados.
  - `ver_pontuacao()`: Exibe pontuação das rodadas.
  - `organizar_dados()`: Finaliza a rodada e calcula pontos.
  - `calcular_pontuacao()`: Avalia combinações especiais.
  - `rodar_programa()`: Controla o fluxo principal do jogo.

- **Dicionários utilizados:**
  - `dados`: Armazena os valores atuais dos dados.
  - `dados_guardados`: Dados que o jogador escolheu guardar.
  - `pontuacao_total`: Pontuação de cada rodada.

## Observações
- O jogo é totalmente interativo via terminal.
- O código está comentado para facilitar o entendimento.
- Não há dependências externas além da biblioteca padrão do Python.

---
Desenvolvido para fins didáticos e de prática em Python.
