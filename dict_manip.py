notes = {}

for i in range(2):
    nom_etudiant = str(input("Saisir le nom de l'étudiant "+str(i+1)))
    note_etudiant = int(input("Saisir la note de l'étudiant "+str(i+1)))
    notes[nom_etudiant] = note_etudiant

for cle, valeur in notes.items():
    if valeur >= 15:
        print('Etudiant', cle, 'admis')
        print('Sa note est ', valeur)
    elif valeur >= 10:
        print('Etudiant', cle, 'admissible après oral')
    else:
        print('Etudiant non admis')
print('une phrase')
