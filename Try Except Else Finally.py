
# try:
#     int(input('Digite um número'))
# except ValueError as error:
#     print(error)

try:
    a = float(input('Digite um nummero'))
    b = float(input('Digite um numero'))
    Resultado = a/b

    print(f' O resultado da divisão é {Resultado}')
except ZeroDivisionError as error:
    print('Divisor não pode ser zero')

else:
    print('Sem erros')


finally:
    print('System is loaded')
    
