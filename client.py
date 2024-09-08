import socket
import threading

# Like the server part, we define changeable variables
Ip = '127.0.0.1'
Port = 8080
Ipv4 = socket.AF_INET
TCP = socket.SOCK_STREAM

# Here we build the client socket
client = socket.socket(Ipv4, TCP)
client.connect((Ip, Port))

def receiver():
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            print(message.decode('utf-8'))
        except:
            print("Error, connection is closing")
            client.close()
            break

def write():
    while True:
        try:
            message = input()  # Fixed input function
            client.send(message.encode('utf-8'))  # Encode message before sending
        except:
            print("Error, could not send message")
            client.close()
            break

receiver_thread = threading.Thread(target=receiver)
receiver_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()
