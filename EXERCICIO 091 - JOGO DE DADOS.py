# Exercício Python 091:
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado
from random import randint
from time import sleep
from operator import itemgetter
print('  JOGANDO DADOS  '  )
jogos = { 'jogador_01':randint(1, 6),
          'jogador_02':randint(1, 6),
          'jogador_03':randint(1, 6),
          'jogador_04':randint(1, 6)}
colocação = ()
print('    lembrando, vence o maior número ...    ')
for k, v in jogos.items():
    print('JOGANDO...')
    sleep(1.5)
    print(f'O {k} tirou o número {v} nos dados.')
    sleep(1)
colocação = sorted(jogos.items(), key = itemgetter(1), reverse = True)
print('**' * 20)
print('  ATENÇÃO PARA A COLOCAÇÃO ...')
for i, v in enumerate(colocação):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} pontos.')




