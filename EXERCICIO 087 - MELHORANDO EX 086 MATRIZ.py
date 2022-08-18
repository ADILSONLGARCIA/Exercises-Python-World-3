# Exercício Python 087:
# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somacoluna = maiorlin1 = 0
for linha in range (0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]:  '))
print('-=' * 15)
for linha in range (0, 3):
    for coluna in range(0, 3):
        print(end = '')
        print(f'[{matriz[linha][coluna]:^5}]', end = '')
# A) A soma de todos os valores pares digitados.
        if matriz[linha][coluna] % 2 == 0:
            somapar = somapar + matriz[linha][coluna]
    print()
# B) A soma dos valores da terceira coluna.
for linha in range(0, 3):
    somacoluna += matriz[linha][2]
# C) O maior valor da segunda linha.
for coluna in range(0, 3):
    if coluna == 0:
         maiorlin1 = matriz[1][coluna]
    elif matriz[1][coluna] > maiorlin1:
        maiorlin1 = matriz[1][coluna]
print('-=' * 15)
print()
print(f'A soma dos números pares da matiz é {somapar}')
print(f'A soma da terceira coluna é {somacoluna}.')
print(f'O maior número da segunda linha é {maiorlin1}')
