num = int(input("Digite um número: "))

if num == 0 or num == 1:
    print("OK")
elif num < 0:
    print("INVALIDO")
else:
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(f'O número {num} é primo')
    else:
        print(f'O número {num} não é primo')
