class Vehicle:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    # def vehicle_info(self):
    #     return self.brand, self.model, self.year, self.price
        
    def info(self):
        print(f"""
            Brand: {self.brand}  
            Model: {self.model}
            Year: {self.year}
            Price: {self.price}€""")
    
class Car(Vehicle):
    def __init__(self, brand, model, year, price, doors):
        super().__init__(brand, model, year, price)
        self.doors = doors

    def info(self):
        super().info()
        print(f"            Number of doors: {self.doors}")

veh1 = Car("Peugeot", "206", 2003, 2000, 4)
print(veh1.info())
# print(str(veh1))
        
# p206 = Car(veh1, 4)
# print(p206.vehicle_info())