# Projeto: Cadastro de Alunos com Dicionários em Python

Este projeto exemplifica como utilizar dicionários e listas para armazenar e manipular dados de múltiplos alunos em Python.

## Funcionamento

- O programa inicializa um dicionário vazio (`alunos`) e uma lista vazia (`dados`).
- Utiliza um laço `for` para coletar informações de 3 alunos.
  - Para cada aluno, solicita o nome e a nota via `input`.
  - Os dados são armazenados no dicionário `alunos` com as chaves `'nome'` e `'nota'`.
  - Uma cópia do dicionário é adicionada à lista `dados` para garantir que cada aluno tenha seu próprio registro independente.
- Ao final, a lista `dados` contém um dicionário para cada aluno, com seus respectivos nomes e notas.
- O programa exibe a lista completa de alunos cadastrados.

## Exemplo de Execução
