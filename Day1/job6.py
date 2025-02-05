class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
    
    def vieillir(self):
        self.age += 1

    def __str__(self):
        return(f"{self.prenom} a {self.age} ans")

    def nommer(self, prenom):
        self.prenom = prenom
        return f"{self} s'appelle {prenom}"


chien = Animal()
chien.age = 5
chien.prenom = "Milou"
# print(str(chien))
# chien.vieillir()
# print(str(chien))

chien.nommer("Gaspar")
print(chien)
chien.age = 10
chien.vieillir()
print(str(chien))