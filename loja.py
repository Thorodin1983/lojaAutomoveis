from automoveis import Automovel
from faker import Faker
import random
import pandas as pd
import sqlalchemy as db
import pyodbc
from bancoDeDados import conexao, tabela

fake = Faker("pt_BR")

#server = 'SERVDB4\\SQLEXPRESS'
#database = "teste"
#username = "sa"
#password = ""

#conn_str = f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}"
conn = pyodbc.connect(conexao())
cursor = conn.cursor()

#conectSqlAchemy = db.create_engine(f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server")

tabela = tabela()

def gerar_automovel():
    return Automovel(
        marca=random.choice(["Toyota", "Ford", "Chevrolet", "Volkswagen", "Honda", "Fiat", "Jeep"]),
        modelo=fake.word().capitalize(),
        ano=random.randint(2000, 2025),
        motorizacao=random.choice(["1.0", "1.0 Turbo", "1,4", "1,5", "1.6", "1.8", "2.0", "3.0 Turbo"]),
        combustivel=random.choice(["Gasolina", "Álcool", "Diesel", "Flex"]),
        cor=fake.color_name(),
        quilometragem=random.randint(0, 200000),
        portas=random.choice([2, 3, 4]),
        transmissao=random.choice(["Manual", "Automática", "Semi Automática"]),
        corDoInterior=random.choice(["Preto", "Bege", "Cinza", "Marrom", "Vermelho"]),
        preco=random.randrange(10000,200000)
    )

dados_veiculos = [gerar_automovel() for _ in range(100)]

dados_veiculos_dict = [{
    "marca": veiculo.marca,
    "modelo": veiculo.modelo,
    "ano": veiculo.ano,
    "motorizacao": veiculo.motorizacao,
    "combustivel": veiculo.combustivel,
    "cor": veiculo.cor,
    "quilometragem": veiculo.quilometragem,
    "portas": veiculo.portas,
    "transmissao": veiculo.transmissao,
    "corDoInterior": veiculo.corDoInterior,
    "preco": veiculo.preco
} for veiculo in dados_veiculos]

df_veiculos = pd.DataFrame(dados_veiculos_dict)
print(df_veiculos)


#try:
for index, veiculo in df_veiculos.iterrows():
    cursor.execute(f"""
        INSERT INTO {tabela}(marca, modelo, ano, motorizacao, combustivel, cor, quilometragem, portas, transmissao, corDoInterior, preco) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
         """, veiculo['marca'], veiculo['modelo'], veiculo['ano'], veiculo['motorizacao'], veiculo['combustivel'], veiculo['cor'], veiculo['quilometragem'], veiculo['portas'],
                       veiculo['transmissao'], veiculo['corDoInterior'], veiculo['preco'])

conn.commit()

cursor.close()
conn.close()

print("Dados inseridos no banco")