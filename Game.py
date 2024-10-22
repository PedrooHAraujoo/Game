import os
def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')
def desenhar_forca(tentativas):
    estagios = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        """
    ]
    print(estagios[6 - tentativas]) 
print('Bem Vindo ao Jogo da Forca!')
palavra_secreta = input('Digite a palavra secreta: ').lower().strip()
lista_de_acertos = ['_' for _ in palavra_secreta]
limpar_terminal()
tentativas = 6
listas_de_letras_tentadas = []
def palavra_descoberta(lista_de_acertos):
    return '_' not in lista_de_acertos

while tentativas > 0 and not palavra_descoberta(lista_de_acertos):
    desenhar_forca(tentativas)
    print(' '.join(lista_de_acertos))
    print(f'Tentativas Restantes: {tentativas}')
    print(f'Letras tentadas: {", ".join(listas_de_letras_tentadas)}')

    letra_do_jogador = input("Digite uma letra: ").lower().strip()
    if len(letra_do_jogador) != 1 or not letra_do_jogador.isalpha():
        print('Digite apenas uma letra.')
        continue

    if letra_do_jogador in listas_de_letras_tentadas:
        print('Você já tentou essa letra, tente novamente.')
    else:
        listas_de_letras_tentadas.append(letra_do_jogador)
        if letra_do_jogador in palavra_secreta:
            for indice, letra in enumerate(palavra_secreta):
                if letra == letra_do_jogador:
                    lista_de_acertos[indice] = letra_do_jogador
        else:
            tentativas -= 1

if palavra_descoberta(lista_de_acertos):
    print(f'Parabéns, você ganhou! A palavra era {palavra_secreta}.')
else:
    desenhar_forca(tentativas)
    print(f'Fim de jogo! A palavra era {palavra_secreta}')
