#Mercado Barbosa
print('e-commerce Barbosa')
produtos = ['', '1-HD', '2-Monitor', '3-Teclado',
            '4-mouse']

valores = [0, 500.00, 5000.00, 300.00, 50.00]

print(f'''
{produtos [1]} R$ {valores[1]}
{produtos [2]} R$ {valores[2]}
{produtos [3]} R$ {valores[3]}
{produtos [4]} R$ {valores[4]}
''')

carrinho = []
total = []

produto_1 = int(input('Produto:'))
produto_2 = int(input('Produto:'))
produto_3 = int(input('Produto:'))
produto_4 = int(input('Produto:'))

carrinho.extend([produtos [produto_1], produtos [produto_2], produtos [produto_3], produtos [produto_4]])
total.extend([valores [produto_1], valores [produto_2], valores [produto_3], valores [produto_4]])

print('***' *20)
print('Produtos', carrinho)
print('R$', sum (total))
print('Obrigado Volte Sempre')