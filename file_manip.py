fichier = open("./files/fichier.jp",'r')
#fichier_ecrit = open("./files/fichier.jp",'w')
compteur = 0

for line in fichier.readlines():
    print(line)
    print('fin de tour')




fichier.close()
#fichier_ecrit.close()
#fichier_ecrit.write(notes)
#ligne = fichier.read(9)
#print(ligne)
#fichier.close()