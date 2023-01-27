import socket
from tkinter import *
from tkinter.messagebox import *

def connexionserveur():
    global connexion_avec_serveur

    connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_avec_serveur.connect((HOST.get(), PORT.get()))
    print("Connexion établie avec le serveur sur le port {}".format(PORT.get()))
    dialogue()

def envoyer(message):
    message=message.encode()
    connexion_avec_serveur.send(message)

def recevoir():
    msg_recu = connexion_avec_serveur.recv(1024)
    msg_recu=msg_recu.decode()
    return msg_recu

def dialogue():
    while 1:
        message = input("Entrez votre message: ")
        print(message)
        envoyer(message)
        msg_recu=recevoir()
        print(msg_recu)

    print("Fermeture de la connexion")
    connexion_avec_serveur.close()


# Création de la fenêtre principale (main window)
Mafenetre = Tk()

Mafenetre.title('Mise en réseau - Client')

# Cadre1 : paramètres serveur
cadre1 = Frame(Mafenetre,borderwidth=2,relief=GROOVE)
cadre1.grid(row=0,column=0,padx=5,pady=5,sticky=W+E)

Label(cadre1, text = "Hôte").grid(row=0,column=0,padx=5,pady=5,sticky=W)
HOST = StringVar()
HOST.set('127.0.0.1')
Entry(cadre1, textvariable= HOST).grid(row=0,column=1,padx=5,pady=5)

Label(cadre1, text = "Port").grid(row=1,column=0,padx=5,pady=5,sticky=W)
PORT = IntVar()
PORT.set(50026)
Entry(cadre1, textvariable= PORT).grid(row=1,column=1,padx=5,pady=5)

ButtonConnexion = Button(cadre1, text ='Connexion au serveur',command=connexionserveur)
ButtonConnexion.grid(row=0,column=2,rowspan=2,padx=5,pady=5)




Mafenetre.mainloop()
