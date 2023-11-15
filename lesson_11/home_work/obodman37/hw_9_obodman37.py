from functools import reduce
# # Reduce
#
# Вивести суму елементів списку з цілих та не цілих чисел
my_list = [1, 2, 3, 4, 0.5, 0.5]
var_reduce = reduce(lambda a, b: a + b if isinstance(b, (int)) else a, my_list, 0)
var_reduce1 = reduce(lambda a, b: a + b if isinstance(b, (float)) else a, my_list, 0)
print(var_reduce)
print(var_reduce1)

# Привести список списків до одновимірного списку використовуючи функцію reduce()
# було: [ [1,2,3], [3,4,5], [6,7,8], ]
# має вийти: [1, 2, 3, 3, 4, 5, 6, 7, 8]

my_list2 = [[1,2,3], [3,4,5], [6,7,8]]
var_reduce2 = reduce(lambda a, b: a + b, my_list2)
print(var_reduce2)

# Filter
# Використовуючи функцію filter() вивести тільки парні числа зі списку.

my_list3 = [1, 2, 3, 4, 5]
my_filter = filter(lambda a: True if a % 2 == 0 else False, my_list3)
print(list(my_filter))

# Використовуючи функцію filter() вивести тільки елементи які мають літеру 'а'.
my_list4 = ["w", "A", "h", "j", "a"]
my_filter1 = filter(lambda a: "a" in a.lower(), my_list4)
print(list(my_filter1))

# Zip
# Зіпнути 2 списки однакової довжини
zipped_list = zip(my_list, my_list4)
print(list(zipped_list))
# Зіпнути 3 списки різної довжини
zipped_list2 = zip(my_list, my_list4, var_reduce2)
print(list(zipped_list2))

# Recursion

# Написати функцію яка виводить ряд Фібоначчі використовуючи рекурсію

def fibonacci_print(n, a=0, b=1):
    if n == 0:
        return
    print(a, end=" ")
    fibonacci_print(n - 1, b, a + b)

fibonacci_print(10)
print()
# Class

# Створити простий, пустий клас без реалізації - PlaceHolder
class PlaceHolder:
    ...

# Створити клас який приймає при ініціалізації 1 параметр і додати метод який друкує цей параметр
class Product:
    def __init__(self, name):
        self.name = name

    def print_self(self):
        print(self.name)
mob_phone = Product("Nokia")
mob_phone.print_self()