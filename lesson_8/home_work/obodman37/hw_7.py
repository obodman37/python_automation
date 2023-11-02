from collections import Counter, namedtuple, defaultdict, deque

def count_most_common(input_str):
    c = Counter(input_str)
    most_common = dict(c.most_common(3))
    return most_common


while True:
    input_str = input(">>>>> Enter the value: ")
    if input_str.isdigit():
        break
    else:
        print("Invalid input. Please enter an integer.")

list = []
for i in input_str:
    list.append(int(i))
print(list)
result = count_most_common(list)
print(result)

print("_" * 50)

Fish = namedtuple('Fish', ['name', 'species', 'tank'])
nemo = Fish('Nemo', 'Clownfish', 'Saltwater')
goldie = Fish('Goldie', 'Goldfish', 'Freshwater')
spike = Fish('Spike', 'Pufferfish', 'Brackish Water')
bubbles = Fish('Bubbles', 'Yellow Tang', 'Saltwater')
fish_dict = spike._asdict()
print(fish_dict)

print("_" * 50)

Fish = namedtuple('Fish', ['name', 'species', 'tank'])

def default_factory():
    return Fish('Unknown', 'Unknown', 'Unknown')

fish_dict = defaultdict(default_factory)
fish_dict['Nemo'] = Fish('Nemo', 'Clownfish', 'Saltwater')
fish_dict['Goldie'] = Fish('Goldie', 'Goldfish', 'Freshwater')
fish_dict['Spike'] = Fish('Spike', 'Pufferfish', 'Brackish Water')

print(fish_dict['Nemo'])
print(fish_dict['Dory'])

print("_" * 50)

d = deque('!')
print(d)
d.append('G')
print(d)
d.appendleft('z')
print(d)
print("Popped element", d.pop())
print(d)
print("Popped left element", d.popleft())
print(d)

print("_" * 50)

def result_logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Result of {func.__name__}: {result}")
        return result
    return wrapper

@result_logger
def add(value):
    result = value + 4
    return result

result = add(6)

print("_" * 50)

def my_decorator_with_args(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(message)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@my_decorator_with_args("Hello from decorator:")
def say_hello():
    print("Hello, world!")

say_hello()