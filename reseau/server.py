import socket
import threading
#from _thread import start_new_thread

#global hote, adr
server = socket.socket()

def carre(x):
    return x**2

def client_threading(hote, adresse):
    print('Nouveau client avec ip:', adresse)
    envoi_client('Le serveur accepte ta demande: ',hote=hote)

    while(True):
        nombre = reception(hote=hote)
        print(nombre)
        square = carre(int(nombre))
        message = f"Le carré de {nombre} est : {square}"
        envoi_client(message=message,hote=hote)

def reception(hote):
    recu = hote.recv(1024)
    recu = recu.decode()
    return recu

def envoi_client(message, hote):
    message=message.encode("utf-8")
    hote.send(message)

try:
    server.bind(('192.168.1.123', 2258))
    server.listen(5)
    print('Serveur crée')
    hote, adr = server.accept()

    print('Nouveau client avec ip:', adr)
    th = threading.Thread(target=client_threading, args=(hote, adr))
    th.start()
except socket.error:
    print("Une erreur s'est produite")
    print(socket.error)
finally:
    print('Fermeture de la connexion')
    server.close()