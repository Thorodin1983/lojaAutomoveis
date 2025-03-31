import socket
import json


def cliente():
    host = 'localhost'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print("Olá! Como posso ajudá-lo hoje?")
    print("Você está procurando um veículo?")
    print("Caso não tenha a intensão de incluir o filtro solicitado, pode deixar em branco")

    marca = input("Qual a marca do veículo?")
    modelo = input("Qual o modelo do veículo?")
    ano_min = input("Qual o ano mínimo?")
    ano_max = input("Qual o ano máximo?")
    combustivel = input(
        "Qual o tipo de combustível? ")
    faixa_preco_min = input("Qual o preço mínimo?")
    faixa_preco_max = input("Qual o preço máximo?")

    filtros = {
        "marca": marca or None,
        "modelo": modelo or None,
        "ano_min": ano_min or None,
        "ano_max": ano_max or None,
        "combustivel": combustivel or None,
        "faixa_preco_min": faixa_preco_min or None,
        "faixa_preco_max": faixa_preco_max or None
    }

    client_socket.sendall(json.dumps(filtros).encode())

    dados_recebidos = client_socket.recv(4096)
    #print(f"Dados recebidos: {dados_recebidos.decode()}")

    try:
        veiculos = json.loads(dados_recebidos.decode())
        if veiculos:
            print("\nVeículos encontrados:")
            for veiculo in veiculos:
                print(f"\nMarca: {veiculo['marca']}")
                print(f"Modelo: {veiculo['modelo']}")
                print(f"Ano: {veiculo['ano']}")
                print(f"Cor: {veiculo['cor']}")
                print(f"Quilometragem: {veiculo['quilometragem']} km")
                print(f"Preço: R${veiculo['preco']:,.2f}")
        else:
            print("Nenhum resultado encontrado para os filtros fornecidos.")
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar os dados recebidos: {e}")
        print("Dados recebidos:", dados_recebidos.decode())

    client_socket.close()

if __name__ == "__main__":
    cliente()