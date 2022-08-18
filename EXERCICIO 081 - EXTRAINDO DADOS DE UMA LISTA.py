# Exercício Python 081:
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
cont = 0
cinco = 5
while True:
    lista.append(int(input('Digite um valor inteiro: ')))
    cont += 1
    resposta = str(input('Deseja continuar [Sim ou Não]?')).strip().upper()[0]
    if resposta in 'Nn':
        break
print()
lista.sort(reverse = True)
print(f'Foram digitados {cont} números.')
print()
print(f'A lista digitada foi... {lista}')
print()
if 5 in lista:
    print(f' O valor cinco foi digitado na lista')
else:
    print('Atenção, o valor de número cinco não consta na lista.')
print()
print('fim')
