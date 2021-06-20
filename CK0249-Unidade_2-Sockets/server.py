from socket import *
import sys

def main():
    server_host = ''
    server_port = 3000

    socket_instance = socket(AF_INET, SOCK_STREAM) #AF_INET = IPv4 SOCK_STREAM =  IP
    socket_instance.bind((server_host, server_port))
    socket_instance.listen(1)
    print("Servidor iniciado e pronto para estabelecer uma nova conexão")

    while True:
        conexao, endereco = socket_instance.accept()
        print("Server conectado por", endereco)

        while True:
            content = conexao.recv(1024).decode()

            if not content: break
            else:
                try:
                    file = open(f'./livros/{content}.txt', 'r')
                    conexao.send(("O Livro '" + content + "' está disponível!").encode())
                except:
                    conexao.send(("O Livro '" + content + "' não está disponível!").encode())
            
        conexao.close()

        print('Servidor pronto para estabelecer uma nova conexão')



if __name__ == '__main__':
    main()


