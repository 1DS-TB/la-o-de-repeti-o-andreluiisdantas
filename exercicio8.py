num = int(input("Digite um número: "))
serie_harmonica = []
serie = 0
soma = 0

if num < 0:
    print("INVALIDO")
elif num == 0:
    print("OK")
else:
    for i in range(1, num + 1):
        serie = f"1/{i}"
        soma += 1 / i
        serie_harmonica.append(serie)

    print(serie_harmonica)
    print(f'A soma é: {soma:.2f}')
