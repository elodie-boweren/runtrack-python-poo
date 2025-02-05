class Cercle:
    def __init__(self):
        self.rayon = 0
        self.diameter = self.rayon * 2
        self.around = self.rayon * 2 * 3.14
        self.surface = self.rayon ** 2 * 3.14

    def changerRayon(self, rayon):
        self.rayon = rayon

    def afficherInfos(self):
        print(f"Le cercle a un rayon de {self.rayon} cm")

    def diametre(self):
        self.diameter = self.rayon * 2
        print(f"diamètre = {self.diameter} cm")

    def circonférence(self):
        self.around = self.rayon * 2 * 3.14
        print(f"circonférence = {self.around} cm")

    def aire(self):
        self.surface = self.rayon ** 2 * 3.14
        print(f"aire = {self.surface} cm²")
      
        

cercle1 = Cercle()
cercle1.changerRayon(4)

# cercle1.aire()
# cercle1.circonférence()
cercle1.afficherInfos(4)





    