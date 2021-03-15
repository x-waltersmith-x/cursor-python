# OOP part 1


# 1
class Vehicle:
    def __init__(self, max_speed, mileage):
        self._max_speed = max_speed
        self._mileage = mileage


# 2
class Bus(Vehicle):
    def set_cap(self, seating_capacity):
        self.seating_capacity = seating_capacity
    def get_cap(self):
        if seating_capacity in self.__dict__:
            return self.seating_capacity
        return None


# 3
school_bus = Bus(100, 200)
check_type = type(school_bus)

print(check_type)


# 4
check_bus = isinstance(school_bus, Vehicle)

print(check_bus)


# 5
class School:
    def __init__(self, school_id, number_of_students):
        self._school_id = school_id
        self._number_of_students = number_of_students
    def get_school_id(self):
        return self._school_id


# 6
class SchoolBus(School, Bus):
    def __init__(self, school_id, number_of_students, max_speed, mileage, seating_capacity, bus_school_color):
        School.__init__(self, school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage)
        self._set_cap(seating_capacity)
        self._bus_school_color = bus_school_color


# 7
class Bear:
    def make_sound(self):
        print("BEAR")


class Wolf:
    def make_sound(self):
        print("Mercedes Benz w124 E500")


i_am_bear = Bear()
i_am_wolf = Wolf()
we_are_animals = (i_am_bear, i_am_wolf)

for animal in we_are_animals:
    animal.make_sound()


# 8
class City():
    def __init__(self, name, population):
        self.name = name
        self.population = population
    def __new__(cls, name, population):
        if population > 1500:
            return super(City, cls).__new__(cls)
        else:
            return 'Your city is too small'
    def __str__(self):
        return f'The population of the city {self.name} is {self.population}'

# 9
Big_City = City("Lviv", 800000)
Small_City = City("Zorah", 890)

print(Big_City)
print(Small_City)


# 10
class Math:
    def __init__(self, sum):
        self.sum = sum
    def __add__(self, variable):
        if self.sum > 10 or variable.sum > 10:
            sum = self.sum * variable.sum
        else:
            sum = self.sum + variable.sum
        return Math(sum)
    def __str__(self):
        return f'{self.sum}'

a = Math(8)
b = Math(5)
c = Math(80)

print(f"Low result is {a + b} and hight result is {c + b}")


# 11
class CallMethod:
    def __call__(self, *args):
        return sum(args)

summary = CallMethod()
print(summary(1, 2, 3, 4, 5))


# 12
class MyOrder:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer
    def __bool__(self):
        return len(self.cart) != 0


first_order = MyOrder(['1', '2', '3'], '4')
second_order = MyOrder([], '1')
check_first = bool(first_order)
check_second = bool(second_order)

print(check_first, check_second)
