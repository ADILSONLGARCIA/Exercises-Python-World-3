lista = ('Familia', 'Amor', 'Esposa', 'Filha', 'Cachorrinha', 'Rosana', 'Ana', 'Milla')
for palavras in lista:
    print(f'\n{palavras.upper():<13} temos: ', end = '')
    for letras in palavras:
        if letras.lower() in 'aeiou':
            print( f'({letras.lower()})', end = '' )
print('\n ' * 2)
print('Nota: Não foi adicionado acentos nas palavras.')

