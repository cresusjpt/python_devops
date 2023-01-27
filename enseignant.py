from personne import Personne

class Enseignant(Personne):

    num_enseignant = ""

    def enseigner(self, matiere):
        print(f"le professeur {self.nom} {self.prenom} enseigne {matiere}")

    def pointer(self, date):
        print(f"{self.nom} {self.prenom} etait présent le {date}")