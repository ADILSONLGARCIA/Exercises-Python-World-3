num = list()
pares = list()
impares = list()
resposta = ''
while True:
    num.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar? [s/n]  '))
    if resposta in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print()
print(f'A lista completa digitada é {num}')
print(f'A lista de números pares digitada é {pares}')
print(f'A lista de números impares digitada é {impares}')
