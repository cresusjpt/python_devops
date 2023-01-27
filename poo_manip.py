from personne import Personne
from enseignant import Enseignant

liliane = Personne(prenom="Jeanpaul", nom='tossou')
liliane.presenter()
#liliane.accident(False)

if liliane.est_vivant():
    print('une action quand on est vivant')
else:
    print('une action quand on est mort')

n,p = liliane.identite()
print(f"le nom de la personne est {n}")