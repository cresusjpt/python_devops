class Personne:
    nom = ""
    prenom = ""
    vivant = True

    def __init__(self, nom, prenom, vivant=True):
        self.nom = str(nom).upper()
        self.prenom = prenom


    def __init__(self, nom, prenom, vivant=False):
            #self.__init__(nom, prenom)
            self.vivant = vivant

    def presenter(self):
        print(f"Je m'appelle {self.nom} {self.prenom}")

    def est_vivant(self):
        return self.vivant
    
    def identite(self):
        return self.nom, self.prenom
    
    def accident(self, vivant):
        self.vivant = vivant
        return self.est_vivant()