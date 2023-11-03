import calendar

lambda_print = lambda value, times=100: print(str(value) * times)

lambda_print('^', 70)
lambda_print(99, 35)

print("_" * 50)

lambda_max = lambda x, y: x if x > y else y
print("Max value:", lambda_max(5,20))

print("_" * 50)

always_ten = lambda: 10
print("Result with lambda always 10:", always_ten())

print("_" * 50)

lst1 = [44, 54, 64, 74, 104]
lst2 = [item + 6 for item in lst1]
print(lst2)

print("_" * 50)

lst3 = [2, 4, 6, 8, 10, 12, 14]
list4 = [x ** 2 for x in lst3]
print(list4)

print("_" * 50)

car_dict = {
    "Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7,
    "Motorcycle": 110
}
list5 = [item.upper() for item in car_dict.keys() if car_dict[item] < 5000]
print(list5)

print("_" * 50)

def month_name(month_number):
    return calendar.month_name[month_number] if month_number >= 1 and month_number <= 12 else "The number of month is not correct"
month_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month_names = list(map(month_name, month_numbers))
print(month_names)