lista = ('Camisa', 45.00, 'Calsa', 99.55, 'Moletom', 75.59, 'Meias', 18.74, 'Regata', 32.99, 'Bermuda', 32, 'Camiseta', 44)
print('=' * 40)
print(f'{"LISTA DE PREÇOS":^40}')
print('=' * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<31}', end='')
    if pos % 2 == 1:
        print ( f'R${lista[pos]:>7.2f}' )
print('=' * 40)