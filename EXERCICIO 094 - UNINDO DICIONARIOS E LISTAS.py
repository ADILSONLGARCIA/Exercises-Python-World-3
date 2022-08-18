# Exercício Python 094:
# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
dados = dict()
cadastro = list()
resp = ''
media = totidade = 0
print('Cadastramento')
print('***' * 10)
while True:
    dados.clear()
    dados['nome'] = str(input('Informe o nome: ')).strip().upper()
    dados['sexo'] = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
    dados['idade'] = int(input('Informe idade: '))
    cadastro.append(dados.copy())
    totidade += dados['idade']
    resp = input ( 'Deseja continuar [S/N]?  ' ).upper ()[0]
    if resp in 'Nn':
        break
# A) Quantas pessoas foram cadastradas
print(f' O número cadastrado foram de {len(cadastro)} pessoas.')
# B) A média de idade
media = totidade / len(cadastro)
print(f' A média de idade das pessoas cadastradas é {media:2.0f} anos.')
# C) Uma lista com as mulheres
for p in cadastro:
    if p['sexo'] in 'Ff':
        print(f'As pessoas do sexo feminino cadastradas foram {p["nome"]}', end = '' )
print()
# D) Uma lista de pessoas com idade acima da média
for p in cadastro:
    if p['idade'] >= media:
        for n, i in p.items():
            print(f'{n} = {i} anos.')
print(cadastro)
