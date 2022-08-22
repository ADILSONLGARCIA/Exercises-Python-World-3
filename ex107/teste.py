import moeda


valor = float(input('Informe o valor do produto:R$ '))
print(f'O valor do produto com aumento de {moeda.aumentar(moeda.aumentar(valor, 10))}' )
