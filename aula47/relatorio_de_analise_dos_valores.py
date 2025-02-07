from matplotlib import pyplot as plt
import numpy as np

# Valores para cada categoria
values = [5, 3, 5, 3, 5]  # Realização Profissional, Família, Liberdade, Contribuição, Conhecimento

# Definir os labels
labels = ['Realização\nProfissional', 'Família', 'Liberdade', 'Contribuição', 'Conhecimento']

# Calcular os ângulos para cada eixo
angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)

# Fechar o gráfico conectando o último valor ao primeiro
values += values[:1]
angles = np.concatenate((angles, [angles[0]]))

# Criar o gráfico radar
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, values, color='red', alpha=0.25)
ax.plot(angles, values, color='red', linewidth=2)

# Adicionar rótulos
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=12)
ax.set_yticklabels([])  # Remover rótulos do eixo radial

# Título
plt.title("Perfil de Valores Pessoais - Resposta 6", fontsize=14, fontweight="bold", y=1.1)

# Exibir o gráfico
plt.show()