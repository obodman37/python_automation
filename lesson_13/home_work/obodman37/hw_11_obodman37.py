"""
# Polymorphism
Створити два класи Car та Bus, обидва мають мати 2 методи wheels() та mode_of_transport(),
які виводять в консоль відповідно, для методу wheels() - 4 та 8, а для методу mode_of_transport() - "Private usage",
"Public usage". Створити об'єкти цих класів, покласти їх у список
а потім пройшовшись циклом for по списку та викликати методи на кожному елементу списку.
"""
class Car():
    def wheels(self):
        return "Car has 4 wheels"

    def mode_of_transport(self):
        return "Private usage"

class Bus():
    def wheels(self):
        return "Bus has 8 wheels"

    def mode_of_transport(self):
        return "Public usage"

"""
Створити клас Vehicle який має два методи desc() та wheels() котрі виводять в консоль певну інформацію. 
Створити 2 дочірніх класи успадкованих від класу Vehicle та перевизначити зазначені 2 методи.
"""
class Vehicle():
    def desc(self):
        return "This is a Vehicle"

    def wheels(self):
        return "It has few wheels"

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__()
        self.brand = brand
        self.model = model
        self.year = year

    def desc(self):
        return "This is a Motorcycle"

    def wheels(self):
        return "It has 2 wheels"

class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__()
        self.brand = brand
        self.model = model
        self.year = year

    def desc(self):
        return "This is an Electric Vehicle"

    def wheels(self):
        return "It has 4 wheels"

"""
# Encapsulation
Створити клас з 2 змінними (_a and __a), Створити об'єкт класу та показати доступ до цих змінних. 
(Очікувано отримаємо помилку при доступі до __а)
"""

class Product():
    def __init__(self, name, selling_price, purchase_price, description):
        self.name = name
        self._selling_price = selling_price
        self.__purchase_price = purchase_price
        self.description = description

    @property
    def protected(self):
        return self._selling_price

    def get_private(self):
        return self.__purchase_price

if __name__ == "__main__":

    obj_Car = Car()
    obj_Bus = Bus()

    my_list = [obj_Car, obj_Bus]
    for item in my_list:
        print(item.wheels(), item.mode_of_transport())

    print("-"*15)
    obj_Vehicle = Vehicle()
    obj_Motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2021)
    obj_ElectricVehicle = ElectricVehicle("Tesla", "Model S", 2023)

    print(f"This is the basic class: Vehicle, with two methods that perform next information: {obj_Vehicle.wheels()}. {obj_Vehicle.desc()}")
    print(f"{obj_Motorcycle.desc()}. {obj_Motorcycle.wheels()}. Name: {obj_Motorcycle.brand}, Model: {obj_Motorcycle.model}, Year: {obj_Motorcycle.year}")
    print(f"{obj_ElectricVehicle.desc()}. {obj_ElectricVehicle.wheels()}. Name: {obj_ElectricVehicle.brand}, Model: {obj_ElectricVehicle.model}, Year: {obj_ElectricVehicle.year}")

    print("-" * 15)

    obj_Product = Product("Huawei Nova 5T", 2000, 1000, "This is mobile phone")
    print(f"Name: {obj_Product.name}, Selling price: {obj_Product._selling_price}, Purchase price: {obj_Product.get_private()} (Private data), Description: {obj_Product.description}")