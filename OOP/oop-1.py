# 1


class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


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
