# nombre1 = 5
# nombre2 = 6
nombre3 = 68
nombre4 = 5.9

class Operation:
    def __init__(self):
        self.nombre1 = 15
        self.nombre2 = 18

    def __str__(self):
        return (f"Le nombre1 est {self.nombre1} et le nombre2 est {self.nombre2}")

    def addition(self, nombre1, nombre2):
        return nombre1 + nombre2
     

#avec __str__
# numbers = Operation()
# print(str(numbers))


# nouvelle_variable = Operation.addition(Operation,5,10)
# print(nouvelle_variable)


