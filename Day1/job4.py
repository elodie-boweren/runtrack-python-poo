nom = "Boweren"
prenom = "Elodie"

class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom 
        self.prenom = prenom
    
    def SePresenter(self):
        print(f"Bonjour, je m'appelle {self.prenom} {self.nom}")


personne1 = Personne("Boweren", "Elodie")
personne2 = Personne("Martin", "Justine")
personne3 = Personne("Gregoire", "Orianne")

personne3.SePresenter()
personne2.SePresenter()

