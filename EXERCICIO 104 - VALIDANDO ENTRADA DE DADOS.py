def leiaInt(msg):
    '''
    Exercício Python 104:
Crie um prgrama que tenhao a função leiaInt(),
que vai funcionar de forma semelhante ‘a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt(‘Digite um n: ‘)

    :param msg: recebe um número inteiro if not informa uma msg de erro.
    :return: retorna o número inteiro.
    '''
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


#Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
