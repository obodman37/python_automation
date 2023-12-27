from abc import ABC, ABCMeta,  abstractmethod

# 1. Створити клас з абстрактним методом. Створити об'єкт даного класу.
class FirstClass():
    @abstractmethod
    def my_method(self):
        pass

obj = FirstClass()
print(obj)
print('_' * 15)

# 2. Створити клас який успадкований від класу ABC або metaclass=ABCMeta і створити його об'єкт.
class MyAbstractClass(ABC):
    pass

obj1 = MyAbstractClass()
print(obj1)
print('_' * 15)

# 3. Створити абстрактний клас з абстрактним методом. Створити новий клас успадкований від абстрактного класу і створіть об'єкт нового класу.

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

class NewClass(AbstractClass):
    def abstract_method(self):
        print("Abstract_method in NewClass")

obj2 = NewClass()
print(obj2)
obj2.abstract_method()
print('_' * 15)

# 4. Створити конструкції try-except для арифметичної операції, роботи з колекціями.

try:
    result = 4 + '3'
except TypeError as e:
    print(f"Error: {e}")

my_list = [1, 2, 3]

try:
    result1 = my_list[3]
except IndexError as e:
    print(f"Error: {e}")

print('_' * 15)

# 5. Створити конструкції try-except-else
try:
    num1 = float(input("Enter first value: "))
    num2 = float(input("Enter second value: "))
    result = num1 / num2
except ZeroDivisionError as e:
    print(f"Error: {e}. Division by zero is impossible.")
except ValueError as e:
    print(f"Error: {e}. Incorrect number entered.")
else:
    print(f"The result of division: {result}")

print('_' * 30)

# 6. Створити конструкції try-except-else-finally
try:
    num3 = float(input("Enter first value: "))
    num4 = float(input("Enter second value: "))
    result = num3 / num4
except ZeroDivisionError as e:
    print(f"Error: {e}. Division by zero is impossible.")
except ValueError as e:
    print(f"Error: {e}. Incorrect number entered.")
else:
    print(f"The result of division: {result}")
finally:
    print("This block is always executed.")

print('_' * 30)

# 7. Створити конструкції try-except-finally
try:
    num5 = float(input("Enter first value: "))
    num6 = float(input("Enter second value: "))
    result = num5 / num6
except ZeroDivisionError as e:
    print(f"Error: {e}. Division by zero is impossible.")
except ValueError as e:
    print(f"Error: {e}. Incorrect number entered.")
finally:
    print("This block is always executed.")

print('_' * 30)

# 8. Створити конструкції try-except з більше ніж трьома except`ами

try:
    value = int(input("Enter the value: "))
    result = 10 / value

except ValueError:
    print("No number entered. Please enter a valid number.")

except ZeroDivisionError:
    print("Division by zero is impossible. Please enter a different number.")

except TypeError:
    print("A type error occurred. Check the correctness of the entered data.")

except Exception as e:
    print(f"Another error: {e}")

else:
    print(f"The result of division: {result}")