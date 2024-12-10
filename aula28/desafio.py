import random
import tkinter as tk

# Instanciando janela
root = tk.Tk()
root.title('Jogo do amigo secreto')

# Definindo o tamanho da janela
largura = 400
altura = 400

# Obtendo o tamanho da tela
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

# Calculando a posição x e y para centralizar
pos_x = (largura_tela - largura) // 2
pos_y = (altura_tela - altura) // 2

# Definindo a geometria da janela centralizada
root.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

# Configurando a cor de fundo da janela
root.configure(bg="#212121")


def get_participants():
    participants = text.get("1.0", "end-1c").split('\n')
    return [p.strip() for p in participants]


def draw_secret_santa(participants):
    friends = participants.copy()
    random.shuffle(friends)

    # Garantir que a lista forme um ciclo válido
    while any(participants[i] == friends[i] for i in range(len(participants))):
        random.shuffle(friends)

    # Retorna os pares na forma circular
    return [(friends[i], friends[(i + 1) % len(friends)]) for i in range(len(friends))]


def display_results(results):
    print('\nAmigo Secreto:')
    for giver, receiver in results:
        print(f'{giver} -> {receiver}')


def shuffle():
    participants = get_participants()
    if len(participants) < 2:
        print('É necessário pelo menos 2 participantes.')
        return

    results = draw_secret_santa(participants)
    return display_results(results)


label = tk.Label(
    root,
    text='Jogo do Amigo Secreto',
    font=('Arial', 20),
    bg='#212121',
    fg='#00ff40'
)
label.pack(pady=20)

main_frame = tk.Frame(
    root,
    bg='#212121',
)
main_frame.pack(pady=0)

text_label = tk.Label(
    main_frame,
    text='Digite o nome dos participantes separados por linha:',
    font=('Arial', 11),
    bg='#212121',
    fg='#00ff40'
)
text_label.pack(pady=5)

text = tk.Text(
    main_frame,
    font=('Arial', 14),
    bg='#2c2c2c',
    fg='#f7f7f7',
    width=30,
    height=10
)
text.pack(pady=5)

button = tk.Button(
    main_frame,
    text='Sortear',
    font=('Arial', 14),
    bg='#2c2c2c',
    fg='#00ff40',
    command=shuffle
)
button.pack(pady=5)

# def get_participants():
#     participants = input('Digite os nomes dos participantes separados por vírgula: ').split(', ')
#     return [p.strip() for p in participants]

# def draw_secret_santa(participants):
#     friends = participants.copy()
#     random.shuffle(friends)

#     # Garantir que a lista forme um ciclo válido
#     while any(participants[i] == friends[i] for i in range(len(participants))):
#         random.shuffle(friends)

#     # Retorna os pares na forma circular
#     return [(friends[i], friends[(i + 1) % len(friends)]) for i in range(len(friends))]

# def display_results(results):
#     print('\nAmigo Secreto:')
#     for giver, receiver in results:
#         print(f'{giver} -> {receiver}')

# def main():
#     participants = get_participants()
#     if len(participants) < 2:
#         print('É necessário pelo menos 2 participantes.')
#         return

#     results = draw_secret_santa(participants)
#     display_results(results)

# if __name__ == '__main__':
#     main()

root.mainloop()
