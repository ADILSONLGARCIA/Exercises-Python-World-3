# Exercício Python 092:
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho
#e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
dados = dict()
print('CADASTRO DO TRABALHADOR')
print('Por favor preencha os dados a seguir. ')
dados['Nome'] = str(input('Informe seu nome: ')).strip().upper()
idade = int(input('Informe o ANO de nascimento: '))
dados['Nascimento'] = datetime.now().year - idade
dados['CTPS'] = int(input('Informe o NÚMERO da CARTEIRA de TRABALHO ( se não tive digite 0): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Informe o ANO de contratação: '))
    dados['Salário'] = float(input('Informe o salário: '))
    dados['Falta_aposenta'] = (35 - (datetime.now().year - dados['Contratação']))
    dados['idade_aposentadoria'] = dados['Falta_aposenta'] + dados['Nascimento']
print('***'*10)
print('Suas informações: ')
print(f'Seu nome é {dados["Nome"]}')
print(f'Você tem {dados["Nascimento"]} anos')
print(f'Faltam {dados["Falta_aposenta"]} anos para se aposentar, e será com a idade de {dados["idade_aposentadoria"]} anos.')
print()
print('Dados armazenados:')
print()
print(dados)
print()
for k, i in dados.items():
    print(f' - {k} tem a informação de {i}')
