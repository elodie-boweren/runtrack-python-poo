class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def perimeter(self):
        return (f"Perimeter = {(self.__length + self.__width) * 2} cm")

    def surface(self):
        return (f"Surface = {self.__length * self.__width} cm²")
    
    def get_length(self):
        return self.__length 
        print()
    
    def get_width(self):
        return self.__width
    
    def set_length(self, value):
        self.__length = value

    def set_width(self, value):
        self.__width = value

class Parallelepipede(Rectangle):
    def __init__(self, rectangle: Rectangle, height):
        super().__init__(rectangle.get_width(), rectangle.get_length())
        self.height = height

    def get_height(self):
        return (f"height = {self.height} cm")
    
    def set_height(self, value):
        self.height = value   

    def volume(self):
        return (f"Volume = {self.get_width() * self.get_length() * self.height} cm3")

rect1 = Rectangle(25,10)
# print(rect1.get_length())
# print(rect1.get_width())
# print(rect1.surface())
# print(rect1.perimeter())

# rect1.set_length(30)
# print(rect1.get_length())

losa1 = Parallelepipede(rect1,20)
print(losa1.get_length())
print(losa1.get_width())
print(losa1.get_height())
# print(losa1.volume())