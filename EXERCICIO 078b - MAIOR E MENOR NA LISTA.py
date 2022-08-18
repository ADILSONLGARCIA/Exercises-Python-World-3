lista = []
maior = menor = 0
for count in range(0, 5):
    lista.append(int(input(f'Digte um valor de número inteiro para a posição {count}: ')))
    if count == 0:
        maior = menor = lista[count]
    else:
        if lista[count] > maior:
            maior = lista[count]
        if lista[count] < menor:
            menor = lista[count]
print()
print(f'Você entrou com os seguintes valores:  {lista}')
print()
print(f'O MAIOR valor encontrado nas entradas foi o Nº {maior} nas posições', end = '  ')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end = '')
print()
print(f'O MENOR valor encontrado nas entradas foi o Nº {menor} nas posições', end = '  ')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end = '')
print()
