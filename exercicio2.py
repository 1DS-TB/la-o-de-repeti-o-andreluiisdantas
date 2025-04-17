num = int(input("Digite um número"))
soma = 0

if num < 0:
    print("INVALIDO")
else:
    while num > 0:
        soma = soma + num
        num = num - 1
    print(soma)