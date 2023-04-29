import socket, time

IP = "192.168.100.60"
PORT = 443

def connect(IP, PORT):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((IP, PORT))
        return client
    except Exception as Error:
        print(Error)

def listen(client):
    while True:
        data = client.recv(1024).decode().strip()
        print(data)
        if  data == "/exit":
            exit()

if __name__ == "__main__":
    while True:
        client = connect(IP, PORT)
        if client:
            listen(client)
        else:
            print("Waiting listening")
            time.sleep(3)