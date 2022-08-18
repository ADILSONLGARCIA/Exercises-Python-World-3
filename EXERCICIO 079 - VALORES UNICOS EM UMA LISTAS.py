# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = list()
while True:
    v = int(input('Digite o valor: '))
    if v not in lista:
        lista.append(v)
    else:
        print('Valor já existe na lista e será desconsiderado.')
    continuar = str(input('Deseja continuar [Sim ou Não]? Digite: ')).upper().strip()[0]
    if continuar == 'N':
        break
lista.sort(reverse = True)
print(lista)

