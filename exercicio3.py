N = int(input("Digite um número "))

if N <= 0:
    print("INVALIDO")
else:
    for i in range(1, 11):
        resultado = N * i

        print(f'{i} * {N} = {resultado}')