# Exercício Python 084:
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves
lista = list()
temporario = list()
maior = menor = p = 0
while True:
    temporario.append(str(input('Informe o nome: ')).strip().upper())
    temporario.append(float(input('Informe o peso: ')))
    if len(lista) == 0:
        maior = menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]
    lista.append(temporario[:])
    temporario.clear()
    resposta = str(input(' Deseja continuar? [S/N] ')).strip().upper()[0]
    if resposta in 'N':
        break
print(f' Os dados cadastrados foram {lista}')
print(f' A quantidade de pessoas cadastradas foram {len(lista)}')
print(f'O maior peso foi o de {maior} Kg. peso de ', end = '')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}]', end = '')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end = '')
for p in lista:
    if p[1] == menor:
        print ( f'[{p[0]}]', end = '' )
