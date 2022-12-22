import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    server.bind(("0.0.0.0", 4444))
    server.listen(5)

    print('Listening...\n')

    client_socket, address = server.accept()
    print('Received from: ' + address[0])
    
    while True:
        data = client_socket.recv(1024).decode()

        if data == "secret\n":
            client_socket.send(b'<segredo>')

    server.close()
except Exception as error:
    print('Error:  ', error)