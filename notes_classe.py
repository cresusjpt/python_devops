notes= {}
moyennes= {}

effectif = int(input("Nombre d'étudiants "))
nbre_note = int(input("Nombre note par matiere "))

for i in range(effectif):
    nom_etudiant = str(input("Saisir le nom de l'étudiant "+str(i+1)+" "))
    compteur = 0
    list_note = []
    
    while compteur != nbre_note:
        compteur+=1
        note_etudiant = float(input("Saisir la note"+str(compteur) +"de l'étudiant "+str(i+1)+" "))
        list_note.append(note_etudiant)
    
    notes[nom_etudiant] = list_note
print(notes)
#calcul de la moyenne de chaque étudiant
for cle,valeurs in notes.items():
    somme=0
    for valeur in valeurs:
        #somme = somme + j
        somme += valeur
    moyennes[cle] = somme/len(valeurs)
print(moyennes)
#calcul de la moyenne de la classe
somme_moyenne = 0
for valeur in moyennes.values():
    somme_moyenne += valeur
moyenne_generale = somme_moyenne/len(moyennes)

#affichage des resultat des étudiants
for nom, moyenne in moyennes.items():
    if moyenne >=15 and moyenne <=20:
        print('Etudiant ', nom, ' admis avec une moyenne de ', moyenne)
    elif not moyenne <= 10:
        print('Etudiant ', nom, ' admissible après oral avec une moyenne de ', moyenne)
    else:
        print('Etudiant ', nom,' non admis avec une moyenne de ', moyenne)
print('La moyenne générale de la classe est ', moyenne_generale)