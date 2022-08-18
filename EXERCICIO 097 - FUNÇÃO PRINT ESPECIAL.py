#Função
def escreve(txt):
    tam = len(txt)
    print('=' * tam)
    print(f'\033[1;30;43m{txt}\033[m')
    print('=' * tam)



# Programa principal
escreve('Olá Mundo! - Hello Word!')
escreve('Estou aqui! I am here!')
