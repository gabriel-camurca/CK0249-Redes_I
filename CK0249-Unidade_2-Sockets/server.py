from socket import *
import sys

def main():
    server_host = ''
    server_port = 3000
    socket_instance = socket(AF_INET, SOCK_STREAM)
    socket_instance.bind((server_host, server_port))
    socket_instance.listen(1)
    print("Servidor iniciado e pronto para estabelecer uma nova conexão")
    while True:
        conexao, endereco = socket_instance.accept()
        print("Server conectado por", endereco)
        try:
            content = conexao.recv(1024).decode()
            filename = content.split()[1]
            file = open(f'./musicas/{filename[1:]}.txt', 'r')
            output_data = file.read()
            conexao.send("HTTP/1.1 200 OK\r\n\r\n".encode())
            for i in range(0, len(output_data)):
                conexao.send(output_data[i].encode())
            conexao.send("\r\n".encode())
            print("Lyrics enviadas com sucesso!")
            conexao.close()
        except IOError:
            print("Não foi possível carregar as lyrics da musica.")
            conexao.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
            conexao.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
            conexao.close()
    socket_instance.close()

if __name__ == '__main__':
    main()


