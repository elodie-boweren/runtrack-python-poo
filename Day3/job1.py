class Town:
    def __init__(self, town_name, number_inhabitants):
        self.__town_name = town_name
        self.__number_inhabitants = number_inhabitants

    def __str__(self):
        return f"{self.__town_name} has {self.__number_inhabitants} inhabitants"
    
    def get_number(self):
        return self.__number_inhabitants
    
    def get_town(self):
        return self.__town_name
    
    def add_person(self):
        self.__number_inhabitants += 1

class Person:
    def __init__(self, person_name: str, age: int, inhabitant : Town):
        self.__person_name = person_name
        self.__age = age
        self.__inhabitant = inhabitant

    def add_inhabitant(self):
        self.__inhabitant.add_person()
   
     
#create town objects
town1 = Town("Paris", 1000000)
print(str(town1))

town2 = Town("Marseille", 861635)
print(str(town2))

#create person objects
person1 = Person("John", 45, town1)
person2 = Person("Myrtille", 4,town1)
person3 = Person("Chloé", 18, town2)

# town1.add_population()
# print(str(town1))

#add a person
person1.add_inhabitant()

print(f"Update of {town1.get_town()} population : {town1.get_number()} inhabitants")

