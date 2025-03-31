import socket
import json
import pyodbc
import sqlite3
from bancoDeDados import conexao, tabela

# Configuração do banco de dados
#server = 'SERVDB4\\SQLEXPRESS'
#database = 'teste'
#username = 'sa'
#password = ''

#conn_str = f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}"
conn = pyodbc.connect(conexao())
cursor = conn.cursor()

tabela = tabela()

def consultar_automoveis(filtros):
    query = f"SELECT * FROM {tabela} WHERE 1=1"

    if 'marca' in filtros:
        query += f" AND marca = '{filtros['marca']}'"
    if 'ano' in filtros:
        query += f" AND ano = {filtros['ano']}"
    if 'combustivel' in filtros:
        query += f" AND combustivel = '{filtros['combustivel']}'"

    cursor.execute(query)
    resultados = cursor.fetchall()

    veiculos = []
    for row in resultados:
        veiculos.append({
            "marca": row[1],
            "modelo": row[2],
            "ano": row[3],
            "motorizacao": row[4],
            "combustivel": row[5],
            "cor": row[6],
            "quilometragem": row[7],
            "portas": row[8],
            "transmissao": row[9],
            "corDoInterior": row[10],
            "preco": row[11]
        })
    return veiculos


def servidor():
    host = 'localhost'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Aguardando conexão...")

    client_socket, client_address = server_socket.accept()
    print(f"Conectado com {client_address}")

    dados_recebidos = client_socket.recv(1024)
    print(f"Dados recebidos: {dados_recebidos.decode()}")

    if dados_recebidos:
        filtros = json.loads(dados_recebidos.decode())
        print(filtros)
        conn = pyodbc.connect(conexao())
        cursor = conn.cursor()

        query = f"SELECT * FROM {tabela} WHERE 1=1"

        if filtros["marca"]:
            query += f" AND marca LIKE '{filtros['marca']}%'"
        if filtros["modelo"]:
            query += f" AND modelo LIKE '{filtros['modelo']}%'"
        if filtros["ano_min"]:
            query += f" AND ano >= {filtros['ano_min']}"
        if filtros["ano_max"]:
            query += f" AND ano <= {filtros['ano_max']}"
        if filtros["combustivel"]:
            query += f" AND combustivel LIKE '{filtros['combustivel']}%'"
        if filtros["faixa_preco_min"]:
            query += f" AND preco >= {filtros['faixa_preco_min']}"
        if filtros["faixa_preco_max"]:
            query += f" AND preco <= {filtros['faixa_preco_max']}"

        cursor.execute(query)
        print(query)
        veiculos = cursor.fetchall()

        conn.close()

        veiculos_encontrados = []
        for veiculo in veiculos:
            veiculos_encontrados.append({
                "marca": veiculo[1],  # Coluna marca - índice 1
                "modelo": veiculo[2],  # Coluna modelo - índice 2
                "ano": veiculo[3],  # Coluna ano - índice 3
                "cor": veiculo[6],  # Coluna cor - índice 6
                "quilometragem": veiculo[7],  # Coluna quilometragem - índice 7
                "preco": veiculo[11]  # Coluna preco - índice 11
            })

        print(f"Veículos encontrados: {veiculos_encontrados}")

        client_socket.sendall(json.dumps(veiculos_encontrados).encode())

    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    servidor()