class Point:
    def __init__(self):
        self.x = 50
        self.y = 150

    def afficherLesPoints(self):
        print(f"{self.x}: {self.y}")

    def afficherX(self):
        print(self.x)
    
    def afficherY(self):
        print(self.y)
    
    def changerX(self, x):
        self.x = x + 50

    def changerY(self, y):
        self.y = y + 60


new_point = Point()
# new_point.afficherLesPoints()
# new_point.afficherX()
# new_point.afficherY()

new_point.changerX(50)
new_point.afficherX()

new_point.changerY(200)
new_point.afficherY()
