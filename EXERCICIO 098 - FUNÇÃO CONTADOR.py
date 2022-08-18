# Exercício Python 098:
# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep

def linha():
    print ( '\033[0;30;45m**\033[m' * 21 )
def contando(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'A contagem de {i} até {f} de {p} em {p}:' )
    sleep(2.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end ='', flush = True)
            sleep(0.5)
            cont += p
        print('\033[1;30;43mFIM!\033[m')
    else:
        cont = i
        while cont >= f:
            print ( f'{cont} ', end = '', flush = True )
            sleep ( 0.5 )
            cont -= p
        print ( '\033[1;30;43mFIM!\033[m' )


# Programa principal
print()
linha()
contando(1, 10, 1)
linha()
contando(10, 0, 2)
linha()
print('Hora de fazer uma contagem personalizada!')
ini = int(input('Início:   '))
fim = int(input('Fim   :   '))
pas = int(input('Passo :   '))
contando(ini, fim, pas)
linha()
