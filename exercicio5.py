
num = int(input("Digite um número: "))
primo = True
if num > 0:
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
    if primo == True:
        print(f'O número {num} é primo')
    else:
        print(f'O número {num} não é primo')
else:
    print("O número precisa ser positivo")


