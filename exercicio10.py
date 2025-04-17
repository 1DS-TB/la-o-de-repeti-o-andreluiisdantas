import math

inicio = int(input("Digite o inicio da lista: "))
fim = int(input("Digite o final da lista: "))

if inicio <= 0 or fim <= 0:
    print("INVALIDO")
else:
    if inicio > fim:
        print("INVÁLIDO")
        print("O segundo número precisa ser maior que o segundo")
    else:
        kaprekar = []
        quadrado = 0
        str_esquerda = ''
        str_direita = ''
        num_esquerda = 0
        num_direita = 0

        for i in range(inicio, fim + 1):
            quadrado = i ** 2
            quadrado = str(quadrado)

            meio = len(quadrado) / 2
            meio = math.floor(meio)

            str_direita = quadrado[meio : len(quadrado)]
            str_esquerda = quadrado[0 : meio]

            if str_direita != '':
                num_direita = int(str_direita)
            if str_esquerda != '':
                num_esquerda = int(str_esquerda)

            soma = num_esquerda + num_direita

            if soma == i:
                kaprekar.append(i)

        if inicio < 1:
            kaprekar.remove(0)

        print(f'O números de kaprekar de {inicio} até {fim} são: {kaprekar}')