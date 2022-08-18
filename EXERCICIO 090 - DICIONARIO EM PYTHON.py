# Exercício Python 090:
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
turma = dict()
t_1a = list()
resposta = 'Ss'
while True:
    turma['Nome'] = str(input('Nome do aluno(a): ')).strip().upper()
    turma['Media'] = float(input('Informe a média: '))
    if turma['Media'] >= 5:
        turma['Situação'] = 'Aprovado'
    else:
        turma['Situação'] = 'Reprovado'
    resposta = str(input('Deseja continuar?[S/N] '))
    if resposta in 'Nn':
        break
t_1a.append(turma.copy())
print('-=' * 15)
for k, v in turma.items():
    print(f'{k} é igual a {v}')
print('Fim!')
