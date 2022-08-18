resp = ''
tupla = ('zero', 'um', 'dois', 'trez', 'quatro',
         'cinco', 'seis', 'sete', 'oito', 'nove',
         'dez', 'onze', 'doze', 'treze', 'quatorze',
         'quinze', 'dezesseis', 'dezessete', 'dezoito',
         'dezenove', 'vinte')
while True :
    numero = int ( input ( 'Por favor digite um número de [0 à 20]:' ) )
    if 0 <= numero <= 20 :
        print ( f'O numero digitado foi o {tupla[numero]}.' )
        resp = input ( str ( 'Deseja continuar[Sim ou Não]? ' ) ).upper ().strip ()[0]
        if resp == 'S':
            break
print ( 'Programa finalizado com sucesso.' )
