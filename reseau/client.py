import socket

client = socket.socket()

def envoi(message):
    message = message.encode()
    client.send(message)

def reception():
    recu = client.recv(1024)
    recu = recu.decode()
    return recu

try:
    client.connect(('192.168.1.123', 2258))

    while 1:
        message = input("Entrez un nombre: ")
        #print(message)
        envoi(message)
        msg_recu=reception()
        print(msg_recu)
except socket.error:
    print('Impossible de se connecter')
finally:
    client.close()