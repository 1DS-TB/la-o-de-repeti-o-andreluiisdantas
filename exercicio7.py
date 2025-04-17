num = int(input("Digite um numero: "))

if num <= 0:
    print("INVALIDO")
else:
    for i in range(num+1):
        print(i*'*')