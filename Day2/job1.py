class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get__length(self):
        return self.__length
    
    def get__width(self):
        return self.__width 
    
    def set__length(self, value):
        self.__length = value

    def set__width(self, value):
        self.__width = value


rect1 = Rectangle(10,5)

# print(rect1.get__length())
# print(rect1.get__width())

rect1.set__length(30)
rect1.set__width(20)

print(rect1.get__length())
print(rect1.get__width())






