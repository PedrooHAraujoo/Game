print('Bem Vindo ao Jogo da Forca!')
palavra_secreta = input('Digite a palavra secreta: ')
lista_de_acertos = [palavra_secreta]
tentativas = 6
listas_de_letras_tentadas = []
def palavra_descoberta(lista_de_acertos):
    return '_' not in lista_de_acertos

while tentativas > 0 and not palavra_descoberta(lista_de_acertos):
    print(' '.join(lista_de_acertos))
    print(tentativas)
    print(listas_de_letras_tentadas)

    letra_do_jogador = input("Digite uma letra: ")

    if letra_do_jogador in listas_de_letras_tentadas:
        print('Você já tentou essa letra, tente novamente.')
    else:
        listas_de_letras_tentadas.append(letra_do_jogador)
        if letra_do_jogador in palavra_secreta:
            for indice, letra_do_jogador in enumerate(palavra_secreta):
                if palavra_secreta[indice] == letra_do_jogador:
                    lista_de_acertos[indice] = letra_do_jogador
        else:
            tentativas -= 1

if palavra_descoberta(lista_de_acertos):
    print(f'Parabéns, você ganhou! A palavra era {palavra_secreta}.')
else:
    print(f'Fim de jogo! A palavra era {palavra_secreta}')
