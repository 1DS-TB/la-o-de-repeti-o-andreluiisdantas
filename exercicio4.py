num = int(input("Digite um número para calcular fatoria: "))

fatorial = 1

for i in range(1, num + 1):
    fatorial *= i
print(f'A fotorial é {fatorial}')