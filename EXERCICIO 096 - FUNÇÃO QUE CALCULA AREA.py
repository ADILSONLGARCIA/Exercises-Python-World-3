# Exercício Python 096:
# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento)
# e mostre a área do terreno.
def área(l, c):
    a = l * c
    print(f' O terreno de largura {l} metros com o comprimento de {c} metros tem uma área de {a} m²')


print('     CONTROLE DE TERRENOS       ')
print('**' * 15)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
área(l, c)
print('**' * 15)
