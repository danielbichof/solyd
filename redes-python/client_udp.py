import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        msg = input("Mensagem: ") + "\n"
        client.sendto(b"DADOS", ("127.0.0.1", 4433))
        data, sender = client.recvfrom(2048)
        print(f"{server[0]}: {data.decode()}")

        if data.decode() == "sair\n" or msg == "sair\n":
            break
except:
    print('Conection error')