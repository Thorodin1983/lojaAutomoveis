#Informar dados de conexão
def conexao():
    server = 'SERVDB4\\SQLEXPRESS'
    database = "teste"
    username = "sa"
    password = ""

    conn_str = f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}"

    return conn_str


#Informar a tabela criada no banco
def tabela():
    tabela = "automoveis"
    return tabela