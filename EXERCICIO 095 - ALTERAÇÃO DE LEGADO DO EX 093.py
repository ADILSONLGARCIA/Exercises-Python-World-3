# No exercício Python 093 foi criado um programa que gerencia o aproveitamento de um jogador de futebol.
# O programa lê o nome do jogador e quantas partidas ele jogou.
# Depois lê a quantidade de gols feitos em cada partida.
# No final, tudo é guardado em um dicionário o total de gols feitos durante o campeonato.
jogador = dict()
partidas = list()
time = list()
while True:
      jogador.clear()
      jogador['nome'] = str(input('Informe o nome do atleta: ')).upper().strip()
      tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?  '))
      partidas.clear()
      for c in range(0, tot):
            partidas.append(int(input(f'        Quantos gols foram feitos na {c+1}ª partida? ')))
      jogador['gols'] = partidas[:]
      jogador['total'] = sum(partidas)
      time.append(jogador.copy())
      while True:
            resp = str(input('Quer continuar [s/n]? ')).upper()[0]
            if resp in 'SN':
                  break
            print('ERRO! Responda apenas S ou N.')
      if resp == 'N':
            break
print('*' * 40)
for k, v in enumerate(time):
      print(f' {k:>3}', end = ' ')
      for d in v.values():
            print(f' {str(d):<15}', end = ' ')
      print()
print('*' * 40)
while True:
      busca = int(input('Mostrar dados de qual jogador [para sair digite 999]? '))
      if busca == 999:
          break
      if busca >= len(time):
          print(f'ERRO! nÃO EXISTE JOGADOR COM ESTE NÚMERO {busca}, TENTE DE NOVO.')
      else:
          print(f' -- LEVANTAMENTO DO JOGADOR {time[busca] ["nome"]}:')
          for i, g in enumerate(time[busca] ['gols']):
                print(f'     No jogo  {i+1}  fez  {g}  gols.')
          print ( '*' * 40 )
print('**' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
      print(f'     => Na partida {i}, fez {v} gols.')
print(f' Foi um total de {jogador["total"]} gols.')
print('<< VOLTE SEMPRE >>')
