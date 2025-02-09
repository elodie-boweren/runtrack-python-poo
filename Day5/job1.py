class Part:
    def __init__(self, name, material):
        self.name = name        
        self.material = material

    def change_material(self, new_material):
        material = new_material

    def __str__(self):
        return f"""The {self.name} is made out of {self.material} """

class Ship:
    def __init__(self, name:str, part=Part):
        self.name = name 
        self.__parts =  {"mast": Part("mast","wood"),                        
                        "sail": Part("sail", "cloth"),
                        "hull": Part("hull","wood"),
                        "headsail": Part("headsail", "cloth"),
                        "helm": Part("helm", "metal")}
        
    
    # def display_state(self):
    #     items = self.__parts.keys()
    #     return f"The {self.name} is made of the following items: {items}"
    
    def display_state(self):
        print(f"Ship's name : {self.name}")
        for i in self.__parts.keys():
            print(f"{i}")
        

    # def replace_part(self, part_name, new_part):
    #     return part_name.pop(new_part)
    

mast = Part("mast","wood")
hull = Part("hull", "wood")
sail = Part("sail", "cloth")
headsail = Part("headsail", "cloth")
helm = Part("helm", "metal")
mast = Part("mast", "metal")
Titanic = Ship("Titanic", "mast")  

# print(str(mast))
# print(str(hull))
# print(str(sail))
# print(str(headsail))
# print(str(helm))

print(Titanic.display_state())
# Titanic.replace_part("mast", "hull")


        
