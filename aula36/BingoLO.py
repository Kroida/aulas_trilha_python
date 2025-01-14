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


class Sorteador:
    def __init__(self, intervalo_min, intervalo_max):
        self.intervalo_min = intervalo_min
        self.intervalo_max = intervalo_max
        self.numeros = list(range(intervalo_min, intervalo_max + 1))
        random.shuffle(self.numeros)
        self.sorteados = set()

    def sortear(self):
        if self.numeros:
            numero = self.numeros.pop(0)
            self.sorteados.add(numero)
            return numero
        return None
      

if __name__ == "__main__":
    # Teste da Cartela
    cartela = Cartela(5, 1, 75)
    print("Cartela Gerada:")
    for linha in cartela.matriz:
        print(linha)
    
    print("\nMarcando o número 20 na cartela:")
    cartela.marcar_numero(20)
    
    print("\nCartela Marcada:")
    for i in range(cartela.tamanho):
        print(f"{cartela.matriz[i]} - {cartela.marcados[i]}")
    
    # Teste do Sorteador
    sorteador = Sorteador(1, 75)
    print("\nNúmeros Sorteados:")
    for _ in range(5):
        numero_sorteado = sorteador.sortear()
        if numero_sorteado:
          print(f"Número sorteado: {numero_sorteado}")
    
    print("\nConjunto de sorteados:")
    print(sorteador.sorteados)