import socket 
## SOCKER relaciona placa de rede com o SO
import sys
## Fornece acesso a variaveis

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexao falhou")
        print("error: {}".format(e))
        sys.exit()
    print("Socket criado com sucesso")

    HostAlvo = input("Digite o host ou ip a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")
    
    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente TCP conectado com sucesso no host: " + HostAlvo + ", na porta: " + PortaAlvo)
        s.shutdown(2)
    except socket.error as e:
        print("A conexao Falhou: " + e)
        sys.exit()

if __name__ == "__main__":
    main()
