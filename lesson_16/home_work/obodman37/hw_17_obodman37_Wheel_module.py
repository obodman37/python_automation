from lesson_13.home_work.obodman37.hw_11_obodman37 import Car as Cr

class NewClass(Cr):
    def __init__(self):
        super().__init__()

    @classmethod
    def class_method(cls):
        return f"This is a class method of {cls.__name__}"

    @staticmethod
    def static_method():
        return "This is a static method"


car_instance = Cr()
print(car_instance.wheels())
print(car_instance.mode_of_transport())

new_class_instance = NewClass()

print(new_class_instance.wheels())
print(new_class_instance.mode_of_transport())
print(NewClass.class_method())
print(NewClass.static_method())