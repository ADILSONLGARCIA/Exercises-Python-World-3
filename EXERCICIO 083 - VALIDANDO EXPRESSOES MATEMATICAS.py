# Exercício Python 083:
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados
# na ordem correta.
expressao =  str(input('Digite uma expressão: '))
pilha = []
for parenteses in expressao:
    if parenteses == '(':
        pilha.append('(')
    elif parenteses == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressão está errada.')
