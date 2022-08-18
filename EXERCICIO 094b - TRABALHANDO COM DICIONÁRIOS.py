#Exercício Python 094b:
# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
pessoas = dict()
galera = list()
media = soma = 0
#lendo nome, sexo e idade de várias pessoas
while True:
    pessoas.clear()
    pessoas['nome'] = str( input( 'Nome: ' ) )
    while True:
        pessoas['sexo'] = str( input( 'Sexo [M/F] : ' ) ).upper().strip()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Por favor digite apenas M ou F.')
    pessoas['idade'] = int( input( 'Idade: ' ) )
    soma += pessoas['idade']
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
    galera.append(pessoas.copy())
    while True:
        resp = str(input('Quer continuar [S/N] ?  ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp in 'N':
        break
print('**' * 30)
# A) Quantas pessoas foram cadastradas
print(f'A) Ao todo temos {len(galera)} pessoas.')
# B) A média de idade
media = soma / len(galera)
print(f'B) A média de idade é {media:5.2f} anos.')
# C) Uma lista com as mulheres
print(f'C) As mulheres cadastradas foram ', end ='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f' {p["nome"]}', end = '' )
print()
# D) Uma lista de pessoas com idade acima da média
print(' D) Lista de pessoas que estão acima da média ')
for p in galera:
    if p['idade'] >= media:
        print('     ', end = ' ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end = '')
        print()
print('<< ENCERRADO >>')
