n = int(input("Digite um número: "))

a = 0
b = 1
if n <= 0:
    print("INVALIDO")
elif n == 1:
    print(a)
elif n== 2:
    print(b)
else:
    s = '0 1 '
    for i in range(n - 2):
        a, b = b, b + a
        s += f'{b} '
    print(s)
