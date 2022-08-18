#Exercício Python 086:
# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
lin01 = [[], [], []]
lin02 = [[], [], []]
lin03 = [[], [], []]
print()
print('-=' * 30)
print()
print('Digite as 03 primeiros dados da primeira linha da matriz.')
print()
for c in range(0, 3):
    lin01[c].append(int(input(f'informe a posição nº{c}: ')))
print()
print('-=' * 30)
print()
print('Digite as 03 dados seguintes da segunda linha na matriz.')
print()
for c in range(0, 3):
    lin02[c].append(int(input(f'informe a posição nº{c}: ')))
print()
print('-=' * 30)
print()
print('Digite as 03 últimos dados da terceira linha na matriz.')
print()
for c in range(0, 3):
    lin03[c].append(int(input(f'informe a posição nº{c}: ')))
print()
print('-=' * 4)
print(f'{lin01[0]}{lin01[1]}{lin01[2]}')
print(f'{lin02[0]}{lin02[1]}{lin02[2]}')
print(f'{lin03[0]}{lin03[1]}{lin03[2]}')

print('-=' * 4)
