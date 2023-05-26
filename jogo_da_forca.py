import random

def selecionar_palavra():
    palavras = ["cachorro", "gato", "elefante", "leão", "tigre", "girafa", "macaco", "zebra", "rinoceronte", "hipopótamo"]
    return random.choice(palavras)

def exibir_palavra(palavra, letras_corretas):
    exibicao = ""
    for letra in palavra:
        if letra in letras_corretas:
            exibicao += letra + " "
        else:
            exibicao += "_ "
    return exibicao

def jogar_forca():
    palavra = selecionar_palavra()
    letras_corretas = []
    tentativas = 6

    print("Bem-vindo ao jogo da forca!")
    print("Adivinhe a palavra oculta adivinhando letras uma por vez. Você tem 6 chances para acertar a palavra completa. Vamos lá!")

    while tentativas > 0:
        print("\n" + exibir_palavra(palavra, letras_corretas))

        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite apenas uma letra válida.")
            continue

        if letra in letras_corretas:
            print("Você já tentou essa letra antes.")
            continue

        if letra in palavra:
            letras_corretas.append(letra)
            if set(palavra) == set(letras_corretas):
                print("\nParabéns! Você acertou a palavra {}!".format(palavra))
                break
        else:
            tentativas -= 1
            print("A letra {} não está na palavra. Você tem {} tentativas restantes.".format(letra, tentativas))

    if tentativas == 0:
        print("\nVocê perdeu! A palavra correta era {}.".format(palavra))

jogar_forca()

