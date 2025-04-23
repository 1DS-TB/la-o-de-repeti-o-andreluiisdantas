N = int(input("Digite um número para calcular fatoria: "))

fatorial = 1

if N == 0:
    print(f'A fotorial é {fatorial}')
elif N < 0:
    print("INVALIDO")
else:
    for i in range(1, N + 1):
        fatorial *= i
    print(f'A fotorial é {fatorial}')
