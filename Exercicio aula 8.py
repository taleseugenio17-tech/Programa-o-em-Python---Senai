#Exercicios condicionais

# Numero = float(input('type a number:'))
# if Numero > 0:
#     print('positivo')
# elif Numero < 0:
#     print('negativo')

# else:
#     print(0)


# Nome = input('Type Your name:')
# Idade = int(input('Type your age:'))

# if Idade < 18:
#     print('You are not allowed to vote')
# elif Idade >= 18:
#     print('Eligible to vote to your representative')

# else:
#     ('See you later')


# Numero = int(input('Type a number'))
# if Numero % 2 == 0:
#     print(f'Esse {Numero} é par')
# else:
#     print(f'Esse {Numero} é impar')


Numero_1 = float(input('Type a number:'))
Numero_2 = float(input('Type a number:'))
Numero_3 = float(input('Type a number:'))

if Numero_1 == Numero_2 == Numero_3:
    print('Triangulo Equilátero')
elif Numero_1 == Numero_2 != Numero_3:
    print('Triângulo Isósceles')
elif Numero_1 != Numero_2 != Numero_3:
    print('Triângulo Escaleno')

else:
    Print('Jogo finalizado')