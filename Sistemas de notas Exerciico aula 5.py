#SIstemas de notas
# notas [float(input('nota:')), float(input('nota:')), float(input('nota:'))]

#ou
notas = [] #lista vazia
nomes = []

nome1 = input('Nome')
n1 = float(input('nota:'))
notas.append(n1) #adicionando nota na lista vazia
nomes.append(nome1)

nome2 = input('Nome')
n2 = float(input('nota:'))
notas.append(n2) #adicionando nota na lista vazia
nomes.append(nome2)

nome3 = input('Noome')
n3 = float(input('nota:'))
notas.append(3) #adicionando nota na lista vazia
nomes.append(nome3)

print(notas)
print(nomes)

#calculando a média
media = sum(notas) / len(notas)
print(media)
maior = notas.index[maior], nomes ()