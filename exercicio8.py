num = int(input("Digite um número: "))
lista = []
serie = 0
soma = 0

if num == 0:
    print("INVALIDO")
else:
    for i in range(1, num+1):
        serie = f"1/{i}"
        soma += 1/i
        lista.append(serie)

    serie_formatada = " + ".join(lista)

    print(f'A série harmônica de {num} é {serie_formatada}')
    print(f'A soma é: {soma:.2f}')