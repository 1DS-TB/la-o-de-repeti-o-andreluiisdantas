lista = []
for num in range(1, 10001):
    soma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            soma_divisores += i
    if soma_divisores == num:
        lista.append(num)
print(f'Os números perfeito de 1 a 10.000 são: {lista}')