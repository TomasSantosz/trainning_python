import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('cliente socked criado com sucesso!!! ')

host = 'localhost'
port = 5433

mensagem = "Olá servidor, td bom?"

try:
    print('cliente: '+ mensagem)
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print("cliente: " + dados)
finally:
    print("Cliente: Fechando a conecão")
    s.close()