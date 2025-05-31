# Resumo da Aula 19 – Dicionários e Programas Interativos em Python 📚🐍

## Introdução

Nesta aula, aprendemos a utilizar **dicionários** em Python para criar programas interativos de controle de informações, como uma agenda telefônica 📞 e um controle de estoque 📦. Os exemplos reforçaram conceitos de entrada e saída de dados, laços de repetição 🔁, condicionais 🔎 e manipulação de estruturas de dados.

---

## Conteúdo Aprendido

### 1. Dicionários em Python 🗂️

- Estrutura de dados que armazena pares **chave: valor**.
- Permite acesso, inserção e atualização rápida de informações.

**Exemplo:**
```python
agenda = {"joao": 12345678, "maria": 87654321}
```

---

### 2. Programa: Agenda Telefônica 📱

O programa permite ao usuário:

- Adicionar contatos (nome e número) ➕
- Listar todos os contatos 📋
- Sair do programa 🚪

**Explicação do código:**

- Um dicionário chamado `agenda` armazena os contatos.
- Um laço `while True` mantém o menu ativo até o usuário escolher sair.
- O usuário pode adicionar um contato, que é salvo no dicionário, ou listar todos os contatos cadastrados.
- O programa verifica se o contato já existe antes de adicionar.
- Ao escolher sair, o programa limpa a tela e exibe uma mensagem de encerramento.

**Exemplo de uso:**
```
~~~ Bem vindo ao menu ~~~
1. Adicionar contato
2. Exibir contatos
3. Sair
Digite a opção desejada (1/2/3): 1
Digite o nome do contato: joao
Digite o número do contato: 12345678
Contato adicionado com sucesso!
```

---

### 3. Programa: Controle de Estoque 🏷️

O programa permite ao usuário:

- Adicionar produtos e suas quantidades ao estoque ➕📦
- Atualizar a quantidade de produtos já existentes 🔄
- Listar o inventário ao final 📑

**Explicação do código:**

- Um dicionário chamado `estoque` armazena os produtos e suas quantidades.
- O usuário insere o nome do produto e a quantidade.
- Se o produto já existe, a quantidade é somada; se não, é criado um novo item.
- O laço termina quando o usuário digita "sair".
- Ao final, o programa exibe todos os produtos e suas quantidades.

**Exemplo de uso:**
```
Digite o nome do produto ("ou sair" para finalizar): arroz
Digite a quantidade de arroz: 10
Digite o nome do produto ("ou sair" para finalizar): feijao
Digite a quantidade de feijao: 5
Digite o nome do produto ("ou sair" para finalizar): arroz
Digite a quantidade de arroz: 2
Digite o nome do produto ("ou sair" para finalizar): sair
arroz: 12
feijao: 5
```

---

## Conclusão 🎯

A aula demonstrou como os dicionários são úteis para armazenar e manipular dados de forma eficiente em Python. Também reforçou a importância dos laços de repetição 🔁 e das estruturas condicionais 🔎 para criar programas interativos e dinâmicos. Os exemplos práticos de agenda telefônica 📞 e controle de estoque 📦 mostraram aplicações reais desses conceitos.