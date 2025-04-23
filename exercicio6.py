N = int(input("Digite um número: "))

if N <= 0:
    print("OK")
else:
    a, b = 0, 1
    s = "0"
    for _ in range(1, N):
        s += f" {b}"
        a, b = b, a + b
    print(s)
