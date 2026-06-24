#Exercicio aula 8 
# Numero = float(input('Digite um número:'))
# if Numero < 0:
#     print(f'O número digitado {Numero} é negativo')
# elif Numero > 0:
#     print(f'O numero digitado {Numero} é positivo')
# else:
#     print(f'O numero digitado {Numero} é zero')

# print('finish')


Nome = input ('Digite o seu nome:')
Idade = int(input('Digite a sua idade:'))

if Idade <= 16:
    print('Não apto a votar')
elif 69 <= Idade <= 18:
    print('Voto Obrigatório')
elif Idade > 70 or Idade == 17:
    print('Voto não obrigatório')

else:
    print('finish')
