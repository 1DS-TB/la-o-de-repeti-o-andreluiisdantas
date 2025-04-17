numero = int(input("Digite um número "))

try:
    for i in range(1, 11):
        print(f'{i} * {numero} = {numero * i}')
except EOFError:
    print("ERRO")