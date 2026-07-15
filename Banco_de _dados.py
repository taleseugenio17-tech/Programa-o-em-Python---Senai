#Relacional e não relacional. Arquivo que armazena dados.
# Relacional -lembra uma planilha excel; Normalmente em SQL. Oracle Postgre SQL;
# Não relacional - lembra um dicionário que tem chave e valor
#Sqlite3 - sem servdor, acesso direto o arquivo, são aplicação menor, no entando utilziado por inumeras empresas incluindo a estação espacial.
#criado digitando no Python; qualquer sistema básico tem o CRUD (creat, read, update, delete)
import squlite3

c = squlite3.connect('bd.db')
cs = c.cursor()
cs.execute('''CREAT TABLE IF NO EXISTS tabela(nome TEXT, idade INTEGER)''')

#ADICIONANDO DADOS
cs.excute('INSERT INTO tabela VALUES(?,?)'. ('Beatriz', 25)) #esse é o cursor
c.commit() #atualiza de fato, toda vez que é feita uma atualização

cs.execute('INSERT INTO TABEL VALUES(?'?)'.('Fernanda', 30)
c.commit()

cs.excutemany () #para inserir varios


