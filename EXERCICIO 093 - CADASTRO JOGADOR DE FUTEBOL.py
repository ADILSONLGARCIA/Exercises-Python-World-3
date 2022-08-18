# Exercício Python 093:
# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato
jogador = dict()
gols = list()
tot = 0
jogador['nome'] = str(input('Informe o nome do atleta: ')).upper().strip()
jogador['time'] = str(input('Informe o nome do time: ')).upper().strip()
tot = int(input('informe a quantidade de jogos: '))
for c in range(0, tot):
      gols.append(int(input(f'Informe quantos gols foram feitos na {c+1}ª partida: ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print(jogador)

