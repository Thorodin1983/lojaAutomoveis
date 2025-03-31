Teste C2S
Modelo dos dados/Criação do objeto automoveis.py
 
Script BD:
CREATE TABLE automoveis (
    id INT IDENTITY(1,1) PRIMARY KEY,
    marca VARCHAR(100),
    modelo VARCHAR(100),
    ano INT,
    motorizacao VARCHAR(50),
	combustivel VARCHAR(50),
    cor VARCHAR(50),
    quilometragem INT,
	portas INT,
	transmissao VARCHAR(50),
	corDoInterior VARCHAR(50)
);

Script para inserção dos dados no banco de dados: loja.py
Utilizei a biblioteca Faker para gerar modelos e cores para os meus veículos;
Conexão pyodbc e inserção de dados com for, retirei o Try except pois os dados estavam sendo gerados corretamente sem interferência exterba;
Biblioteca Random parar escolher e gerar números aleatórios conforme o range para anmo, porta e quilometragem, nos outros campos eu passei uma lista e pedi para ele escolher aleatoriamente.
Biblioteca pandas para montar o data frame

Dados inseridos no BD
 

Estrutura MCP para conexão das informações

O servidor vai interpretar as requisições em uma porta específica(que eu deixei como 12345), receber os filtros, consultar o banco de dados e retornar os resultados para o cliente.

O cliente vai enviar filtros como uma string ou JSON, e receber os resultados do servidor.

Prtojeto CMD
Apenas uma requisição por execução, primeiro executar o servidor para receber as infos e depois o client para enviar sua solicitação para o servidor
Existe uma interçaão básica para o usuário informar os dados que precisa para filtrar no banco de dados
E assim ele fornece as infos, conectando o cliente ao servidor


