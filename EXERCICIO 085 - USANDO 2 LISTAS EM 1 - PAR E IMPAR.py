lista = [[], []]
dados = 0
for c in range(1, 8):
    dados = int(input('Digite um número: '))
    if dados % 2 == 0:
        lista[0].append(dados)
    else:
        lista[1].append(dados)
lista[0].sort()
lista[1].sort()
print(f'A lista com os valores pares é {lista[0]}')
print(f'A lista com os valores impares é {lista[1]}')
