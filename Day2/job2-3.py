class Book:
    def __init__(self, title, author, number_of_pages, available = True):
        self.__title = title
        self.__author = author
        self.__number_of_pages = number_of_pages
        self.__available = available

    def get_title(self):
        return self.__title
    
    def set_title(self, value):
        self.__title = value

    def get_author(self):
        return self.__author
    
    def set_author(self, value):
        self.__author = value

    def get_number_of_pages(self):
        return self.__number_of_pages
    
    def set_number_of_pages(self,value):
        if isinstance(value, int) and value > 0:
            self.__number_of_pages = value
        else : print("Number of pages must be a positive integer")

    def check_availability(self):
        return self.__available
    
    def borrow(self, value= False):
        if self.__available == True:
            self.__borrowed = True
            return self.__available(False)
        else : print("The book is currently unavailable, it cannot be borrowed")
    
    # def bring_back(self):


        
    

book1 = Book("book","denise",50, True)
book1.get_title()
# print(book1.get_title())
book1.set_title("extraordinary")

# print(book1.get_title())
book1.set_author("Mad_person")
# print(book1.get_author())
# print(book1.get_number_of_pages())

book1.set_number_of_pages(68)
# print(book1.get_number_of_pages())

print(book1.check_availability())

book1.borrow()






    
