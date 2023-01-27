from math import sqrt
#1.1
temps = 6.892
distance = 19.7

vitesse = distance / temps
print('La vitesse est ', vitesse)

#1.2
nom = input('Saisir un nom ')
age = input(' Saisir age ')

nom = str(input('Saisir un nom'))
age = int(input('Saisir un age'))

#2.1
flottant = float(input('Saisir un nombre floattant'))
if flottant >=0:
    print(f"la racine de {flottant} est", sqrt(flottant))

#2.2
mot_1 = str(input('Saisir mot 1: '))
mot_2 = str(input('Saisir mot 2: '))

print(mot_1, ' plus petit') if mot_1 < mot_2 else print(mot_2, ' plus petit')

