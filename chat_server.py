import socket
import threading

# Here we define changeable variables
Ip = '0.0.0.0'
Port = 8080
Ipv4 = socket.AF_INET
TCP = socket.SOCK_STREAM

# Here we build the server socket
server_socket = socket.socket(Ipv4, TCP)
server_socket.bind((Ip, Port))
server_socket.listen()

# Here we put an array to take client information
clients = []

# Functions to receive and broadcast messages and accept users
def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            clients.remove(client)
            client.close()

def handler(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            broadcast(message)
        except:
            break
    if client in clients:
        clients.remove(client)
    client.close()

def receiver():
    while True:
        client, address = server_socket.accept()
        print(f"{str(address)} was connected")
        clients.append(client)
        thread = threading.Thread(target=handler, args=(client,))
        thread.start()

print("Server is online...")
receiver()
