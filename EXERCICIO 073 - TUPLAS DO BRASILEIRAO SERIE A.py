brasileirao = ('', 'Palmeiras', 'Corinthians', 'Fluminense', 'Atlético-MG', 'Athletico-PR', 'Flamengo',  'Internacional', 'Bragantino',
                'Santos', 'São Paulo', 'Botafogo', 'Ceará', 'Coritiba', 'Goiás', 'América-MG', 'Avaí', 'Cuiabá','Atletico-GO',  'Juventude', 'Fortaleza')
print(f'Os cinco primeiro colocados no Brasileirão serie-a são respectivamente: {brasileirao[1:6]}')
print(f'Na bandeirinha nas quatro ultimos colocados no Brasileirão serie-a com risco de rebaixamento são: {brasileirao[-4:]}')
print(f'Em orde alfabética os 20 primeiros aparece assim: {sorted(brasileirao)}')
print(f'O Bragantino está na {brasileirao.index("Bragantino")}ª posição.')
