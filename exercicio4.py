num = int(input("Digite um número para calcular fatoria: "))

fatorial = 1

if num == 0:
    print(f'A fotorial é {fatorial}')
elif num < 0:
    print("INVALIDO")
else:
    for i in range(1, num + 1):
        fatorial *= i
    print(f'A fotorial é {fatorial}')