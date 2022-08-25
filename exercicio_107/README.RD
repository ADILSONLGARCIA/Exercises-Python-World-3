Estou com um problema, tentando resolver.

Criei um módulo de nome "exercicio_107" e um pacote de nome "moeda.py":

'''
def aumentar(valor, taxa):
    res = valor + (valor * taxa/100)
    return res
'''

Importei o pacote em um arquivo "teste.py":

'''
import moeda

valor = float(input('Informe o valor do produto:R$ '))
print(f'O valor do produto com aumento de {moeda.aumentar(valor, 10 )}')
'''

E estou com uma falha quando rodo o teste que diz assim:

**ModuleNotFoundError: No module named 'moeda'**
