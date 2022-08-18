#Exercício Python 080:
# Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.
valores = []
for cont in range(0, 5):
    numero = int(input('Digite um valor inteiro: '))
    if cont == 0 or numero > valores[-1]:
        valores.append(numero)
    else:
        pos = 0
        while pos < len(valores):
            if numero <= valores[pos]:
                valores.insert(pos, numero)
                break
            pos =+ 1
print()
print(f'Os valores em ordem são {valores}')
