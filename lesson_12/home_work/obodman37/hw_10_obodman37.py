"""1. Створити простий, пустий клас без реалізації - BaseClass"""

class BaseClass:
    ...

"""2. Створити клас який успадковується від класу з пункта 1. 
Додади для ініціалізації ще 1 параметр і ще один метод для виведення нового параметра."""

class Product(BaseClass):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def get_name(self):
        return print(self.name)
"""3. Створити клас з методом return_fields() який нічого не повертає (... | pass)"""

class Product1():
    def return_filds(self):
        ...

"""4. Створити клас, який прийматиме 2 параметри, успадкований від класу з пункту 3 
і перевизначити метод return_fields() який виведе поля класу."""

class Product2(Product1):
    def __init__(self, name, price):
        super().__init__()
        self.name = name
        self.price = price
    def return_filds(self):
        print(f"Name: {self.name}, Price: {self.price}")

"""5. Створити клас, який прийматиме 3 параметри, успадкований від класу з пункту 3 
і перевизначити метод return_fields() який виведе поля класу."""

class Product3(Product1):
    def __init__(self, name, price, description):
        super().__init__()
        self.name = name
        self.price = price
        self.description = description

    def return_filds(self):
        print(f"Name: {self.name}, Price: {self.price}, Description: {self.description}")