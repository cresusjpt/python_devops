##-----Importation des Modules-----##
from tkinter import *


##----- Définition des Variables globales -----##
cases = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

joueur = 1            # On commence par J1. J2 est associé au nombre -1
n = 1                 # Numéro du tour de jeu
somme = 0             # Somme des cases/numéro du joueur gagnant


##----- Définition des Fonctions -----##
def verif(tableau):
    """Calcule des sommes de chaque ligne/colonne/diagonale pour
        vérifier l'alignement. Elle renvoie le n° du gagnant."""
    sommes = [0,0,0,0,0,0,0,0]             # Il y a 8 sommes à vérifier
    # Les lignes :
    sommes[0] = sum(tableau[0])
    sommes[1] = sum(tableau[1])
    sommes[2] = sum(tableau[2])
    # Les colonnes
    sommes[3] = tableau[0][0]+tableau[1][0]+tableau[2][0]
    sommes[4] = tableau[0][1]+tableau[1][1]+tableau[2][1]
    sommes[5] = tableau[0][2]+tableau[1][2]+tableau[2][2]
    # Les diagonales
    sommes[6] = tableau[0][0]+tableau[1][1]+tableau[2][2]
    sommes[7] = tableau[0][2]+tableau[1][1]+tableau[2][0]

    for i in range(8):                     # Parcours des sommes
        if sommes[i] == 3:
            return 1
        elif sommes[i] == -3:
            return -1
    return 0


def demande(numero):
    """Cette fonction renvoie la case dans laquelle le joueur joue."""
    if numero == 1:
        print('Au tour du joueur n°1')
    else:
        print('Au tour du joueur n°2')
    ligne = int(input('Numéro de ligne ?'))
    colonne = int(input('Numéro de colonne ?'))
    return ligne, colonne


def affichage(tableau):
    """Cette fonction affiche à l'écran chaque ligne d'un tableau."""
    n = len(tableau)
    for i in range(n) :
        print(tableau[i])
##-----Création de la fenêtre-----##
fen = Tk()
fen.title('Morpion')


##-----Création des zones de texte-----##
message=Label(fen, text='Ici du texte.')
message.grid(row = 0, column = 0, columnspan=2, padx=3, pady=3, sticky = W+E)


##-----Création des boutons-----##
bouton_quitter = Button(fen, text='Quitter', command=fen.destroy)
bouton_quitter.grid(row = 2, column = 1, padx=3, pady=3, sticky = S+W+E)

bouton_reload = Button(fen, text='Recommencer')
bouton_reload.grid(row = 2, column = 0, padx=3, pady=3, sticky = S+W+E)


##-----Création du canevas-----##
dessin=Canvas(fen, bg="white", width=301, height=301)
dessin.grid(row = 1, column = 0, columnspan = 2, padx=5, pady=5)


##-----La grille-----##
lignes = []
for i in range(4):
    lignes.append(dessin.create_line(0, 100*i+2, 303, 100*i+2, width=3))
    lignes.append(dessin.create_line(100*i+2, 0, 100*i+2, 303, width=3))


##-----Programme principal-----##
affichage(cases)                         # Affichage dans la console

while somme == 0 and n <= 9:
    [ligne, colonne] = demande(joueur)   # demande() renvoie 2 valeurs
    while cases[ligne][colonne] != 0:    # Recherche d'une case vide
        print('Case occupée')
        [ligne, colonne] = demande(joueur)
    cases[ligne][colonne] = joueur       # On place 1 ou -1 dans cases
    affichage(cases)

    somme = verif(cases)                 # Vérification de l'alignement
    joueur = -joueur                     # Passage au joueur suivant
    n += 1                               # Passage au tour suivant

if somme == 1:
    print('Bravo joueur 1 !')
elif somme == -1:
    print('Bravo joueur 2 !')
else:
    print('Match nul !')
fen.mainloop()   