N = int(input("Digite um número: "))

a = 0
b = 1
if N <= 0:
    print("INVALIDO")
elif N == 1:
    print(a)
elif N == 2:
    print(b)
else:
    s = '0, 1'
    for i in range(N - 2):
        a, b = b, b + a
        s += f', {b}'
    print(s)
