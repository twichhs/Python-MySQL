import mysql.connector

# Estabelecendo a conexão com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Joao-14_12',
    database='logins',
)

# Criando um cursor para executar comandos
cursor = conexao.cursor()

# Dados a serem inseridos
Username = ""
Password = ""

# Comando SQL com parâmetros
# Pensa que o comando é o que você digitaria no terminal do mysql, é literalmente isso só que pelo Python
comando = 'INSERT INTO usuários (username, codepass) VALUES (%s, %s)'
# Os valores tão convertidos em string, e no banco de dados como varchar(30)
# Executando o comando com os dados
cursor.execute(comando, (Username, Password))
# inicialmente o segundo parenteses fica fechado, mas aqui queremos passar o nome das variaveis que serão os dados que vão ser inseridos
# Confirmando as alterações no banco de dados
conexao.commit()

# Fechando o cursor e a conexão
cursor.close()
conexao.close()