num = (int(input('Informe um número qualquer: ')),
       int(input('Informe mais um número qualquer: ')),
       int(input('Informe outro número qualquer: ')),
       int(input('Informe o último número qualquer: ')))
print('')
print('Analizando...')
print(f'Os quatro numeros armazenados foram {num}')
if 9 in num:
       print(f'O valor 9 apareceu {num.count(9)} vezes.')
else:
       print ( 'O número 9 não foi digitado.' )
if 3 in num:
       print(f'O primeiro valor de número 3 foi digitado na {num.index(3)+1}ª posição.')
else:
       print('O número 3 não foi digitado.')
print('O valores pares são:', end = ' ')
for n in num:
       if n % 2 == 0:
              print( n, end = ',')
