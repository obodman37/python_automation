import csv, json
# Створити файл та записати в нього рядок.

file = open("obodman.txt", 'w')
file.write('Hello, this is my homework № 15')
file.close()

# Прочитати створений файл та вивести на консоль вміст файлу

file = None

try:
    file = open("obodman.txt", 'r', encoding='windows-1251')
    content = file.read()
    print(content)
except FileExistsError as e:
    print(e)
finally:
    file.close()

# Додати ще один рядок до створеного файлу.

file_name = "obodman.txt"
with open(file_name, 'a', encoding='windows-1251') as file:
    file.write('\nHow is it going??? This is second line.')
    file.close()

print('_' * 15)
# Прочитати всі рядки з файлу та вивести на консоль.
file_name = "obodman.txt"

with open(file_name, 'r', encoding='windows-1251') as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())

print('_' * 15)
# Використайте прикріплений файл csv та прочитайте його за допомогою модулю csv.
with open('SampleCSVFile_11kb.csv') as dm:
    data = csv.reader(dm)
    for line in data:
        print(line)

print('_' * 15)
# Використайте прикріплений файл json та прочитайте його за допомогою модулю json.
json_file = "sample2.json"

with open(json_file, "r") as js_file:
    data = json.load(js_file)
    print(data)
    print(json.dumps(data, indent=2))
