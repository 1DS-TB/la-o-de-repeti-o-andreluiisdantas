num = int(input("Digite um número "))

if num < 0:
    print("INVALIDO")
else:
    if num == 0:
        print("Tabuada do 0 não existe.")
    else:
        for i in range(1, 11):
            resultado = num * i
            print(f'{i} * {num} = {resultado}')