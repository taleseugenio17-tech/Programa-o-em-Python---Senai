# para limitar o loop é necessário adicionar c+1, diferente do for o while precisa de um contador, por isso é um loop infinito
# c = 0
# while c <= 9:
#     print(c)
#     c = c+1 

# c = 0
# while c <= 1000:
#     print(c)
#     c = c+1


# Nomes = []
# i = 0
# while i < 10:
#     Nome = input(f'Type your name: {i+1}: ')
#     Nomes.append(Nome)
#     i += 1

# print('Lista de pessoas')

# i = 0 
# while i < len(Nomes):
#     print(Nomes[i])
#     i += 1

#Sistemas de Notas aluno

for i in range(3):
    senha = input('Digite sua senha')
    if senha == '123':
        print('Bem vindo ao sistema de notas')

        Notas =[]
        for a in range (3):
            n1 = float(input('Digite nota do aluno:'))
            Notas.append (n1)
            

        i = sum (Notas) / len(Notas)


        print('Média do aluno:',round(i,2))
        break

else:
    print('Senha bloqueada')




