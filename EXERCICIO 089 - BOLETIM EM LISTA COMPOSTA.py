#Exercício Python 089:
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e
# permita que o usuário possa mostrar as notas de cada aluno individualmente.
média = 0
boletim = []
print('***' * 30)
while True:
    nome = str(input("Nome: "))
    nota_1 = float(input('Nota 01: '))
    nota_2 = float(input('Nota 02: '))
    média = (nota_1 + nota_2) / 2
    boletim.append([nome, [nota_1, nota_2], média])
    resp = str(input('Deseja Continuar [s/n]? ')).strip().upper()[0]
    if resp in 'Nn':
        break
print('***' * 31)
print('***' * 9, 'LISTA BOLETIM', '***' * 9)
print('***' * 31)
print(f'{"Nº.":<4}{"Nome":<10}{"Média":>8}')
print(' ')
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opção = int(input('Mostrar notas de qual aluno (999 interrompe)? '))
    if opção == 999:
        print('FIM!')
        break
    if opção <= len(boletim) -1:
        print(f'Notas de {boletim[opção] [0]} são {boletim[opção][1]}')
print('Fim!')
