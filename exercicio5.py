N = int(input("Digite um número: "))

if N <= 0 or N == 1:
    print(f'O número {N} não é primo')
else:
    primo = True
    for i in range(2, N):
        if N % i == 0:
            primo = False
            break
    if primo:
        print(f'O número {N} é primo')
    else:
        print(f'O número {N} não é primo')
