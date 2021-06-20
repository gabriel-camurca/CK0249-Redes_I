from socket import *

def main():
    server_host = 'localhost'
    server_port = 3000

    socket_instance = socket(AF_INET, SOCK_STREAM)
    socket_instance.connect((server_host, server_port))

    msg = input("Digite o nome do livro que deseja procurar: ")
    msg_encoded = msg.encode()

    socket_instance.send(msg_encoded)

    content = socket_instance.recv(1024).decode()

    print("Recebi:", content)

    socket_instance.close()

if __name__ == '__main__':
    main()