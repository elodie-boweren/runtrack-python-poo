class Personnage:
    def __init__(self):
        self.x = 120
        self.y = 100
    
    def gauche(self):
        self.x -= 5

    def droite(self):
        self.x += 5

    def haut(self):
        self.y -= 5
    
    def bas(self):
        self.y += 5

    def position(self):
        print(f"( {self.x} , { self.y })")


perso = Personnage()
perso.position()

perso.gauche()
perso.position()

perso.bas()
perso.position()