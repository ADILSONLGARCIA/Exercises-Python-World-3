# Exercício Python 099:
# Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep

def mor(* num):
    contador = maior = 0
    print('**' * 30)
    print('Analisando os valores ... ')
    for valor in num:
        print(f'{valor}  ', end ='', flush = True)
        sleep(0.3)
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    print(f'Foram informados {contador} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


mor(2, 5, 7, 8, 18)
print()
mor(55, 44, 2, 1)
print()
mor(33, 5, 2, 55, 9)
