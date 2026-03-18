valor = int(input('insira: '))
d = 1
divisivel = []

while d <= valor:
    if valor % d == 0:
        divisivel.append(d)
    d += 1

print(divisivel, valor)