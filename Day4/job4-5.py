class Form:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def surface(self):
        return 0
    
class Rectangle(Form):
    def __init__(self, form):
        super().__init__(form.side1, form.side2)
        self.length = form.side1
        self.width = form.side2

    def __str__(self):
        return f"""
                    Length = {self.length} cm
                    Width = {self.width} cm
                    Surface = {self.surface()} cm² 
                    """
    
    def surface(self):
        return self.length * self.width

class Circle(Form):
    def __init__(self, form, radius):
        super().__init__(form.side1, form.side2)
        self.radius = radius

    def surface(self):
        return self.radius**2 * 3.14


form1 = Form(10, 20)   

rect1 = Rectangle(form1)
rect1.surface()
print(rect1.surface())
print(str(rect1))

circle1 = Circle(form1, 6)
circle1.surface()
print(circle1.surface())
        

