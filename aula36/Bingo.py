import random

class Cartela:
    def __init__(self, tamanho, intervalo_min, intervalo_max):
        self.tamanho = tamanho
        self.intervalo_min = intervalo_min
        self.intervalo_max = intervalo_max
        self.matriz = []
        self.marcados = []
        self.gerar_cartela()

    def gerar_cartela(self):
        # Cria lista de números únicos dentro do intervalo e embaralha
        numeros = random.sample(range(self.intervalo_min, self.intervalo_max + 1), self.tamanho * self.tamanho)
        
        # Cria a matriz da cartela
        self.matriz = [numeros[i:i + self.tamanho] for i in range(0, len(numeros), self.tamanho)]
        
        # Marca o meio como livre (0)
        meio = self.tamanho // 2
        self.matriz[meio][meio] = 0 

        # Inicializa matriz de marcados como False
        self.marcados = [[False for _ in range(self.tamanho)] for _ in range(self.tamanho)]

    def marcar_numero(self, numero):
      for i in range(self.tamanho):
        for j in range(self.tamanho):
          if self.matriz[i][j] == numero:
             self.marcados[i][j] = True

    def verificar_vitoria(self):
      # Verificar linhas
      for row in self.marcados:
        if all(row):
          return True
      
      # Verificar colunas
      for j in range(self.tamanho):
        if all(self.marcados[i][j] for i in range(self.tamanho)):
          return True
      
      # Verificar diagonais
      if all(self.marcados[i][i] for i in range(self.tamanho)) or all(self.marcados[i][self.tamanho - 1 - i] for i in range(self.tamanho)):
        return True

      return False