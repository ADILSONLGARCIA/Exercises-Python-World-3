def notas(*n, sit=False):
    '''
    -> Guardando notas em um dicionário e analizando as notas.
    :param n: entrada de várias notas
    :param sit: este é opcional com True ou False
    :return: retorna os valores das notas contidas no dicionário
    '''
    r = dict()
    r['Total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['sitiação'] = 'BOA'
        elif r['média'] >= 5:
            r['sitiação'] = 'RAZOÁVEL'
        else:
            r['sitiação'] = 'RUIM'
    return r

#Programa principal
resp = notas(9.5, 0.6, 9.75, 7.4, sit=True)
print(resp)
