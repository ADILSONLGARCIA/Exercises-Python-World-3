# Exercício Python 101:
# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(ano):
    from datetime import date
    agora = date.today().year
    idade = agora - ano
    if idade < 16:
        return f'A sua idade é {idade} anos e o voto é NEGADO para as pessoas que se encontram com idade menor de 16 anos.'
    elif 16 <= idade < 18 or idade > 65:
        return f'A sua idade é {idade} anos e o voto é OPCIONAL para as pessoas que se encontram com idade entre 16 e 18 anos e maior que 65 anos.'
    else:
        return f'A sua idade é {idade} anos e o voto é OBRIGATÓRIO para as pessoas que se encontram com idade entre 18 e 65 anos.'


ano_nasc = int(input('Digite o ano de nascimento: '))
print(voto(ano_nasc))
