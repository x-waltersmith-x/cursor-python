# 1


class Vehicle:
    def __init__(self, max_speed, mileage):
        self._max_speed = max_speed
        self._mileage = mileage


# 2


class Bus(Vehicle):
    def set_cap(self, seating_capacity):
        self._seating_capacity = seating_capacity
    def get_cap(self):
        if "_seating_capacity" in self.__dict__:
            return self._seating_capacity
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