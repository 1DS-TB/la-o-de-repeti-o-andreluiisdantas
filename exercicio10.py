import math

try:
    inicio = int(input("Digite o inicio da lista: "))
    fim = int(input("Digite o final da lista: "))

    if inicio <= 0 or fim <= 0:
        print("INVALIDO")
        print("OK") 
    elif inicio > fim:
        print("INVÁLIDO")
        print("O segundo número precisa ser maior que o primeiro")
        print("OK")
    else:
        kaprekar = []

        for i in range(inicio, fim + 1):
            quadrado = str(i ** 2)
            meio = math.floor(len(quadrado) / 2)

            str_direita = quadrado[meio:]
            str_esquerda = quadrado[:meio]

            num_direita = int(str_direita) if str_direita else 0
            num_esquerda = int(str_esquerda) if str_esquerda else 0

            if num_direita + num_esquerda == i:
                kaprekar.append(i)

        print(f'O números de kaprekar de {inicio} até {fim} são: {kaprekar}')
except EOFError:
    print("ERRO")
