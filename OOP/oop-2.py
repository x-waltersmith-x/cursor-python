import dataclasses
import collections


# 1.
class Laptop:
    def __init__(self, battery, brand):
        self.battery = Battery
        self.brand = brand


class Battery:
    def __init__(self, capacity):
        self.capacity = capacity


# 2.
class Guitar:
    def __init__(self, strings, type):
        self.strings = strings
        self.type = type


class GuitarString:
    def __init__(self, material):
        self.material = material


GuitarString.material = 'steel'
guitar = Guitar(GuitarString.material, 'Electric')
print(f'This is {guitar.type} guitar with {guitar.strings} strings')


# 3
class Calc:
    @staticmethod
    def add_nums(x, y, z):
        return x + y + z


print(Calc.add_nums(10, 12, 23))


# 4.
class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        return Pasta(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return Pasta(['bacon', 'parmesan', 'eggs'])


# 5
class Concert:
    max_visitors_num = 0

    def __init__(self, visitors_count=0):
        self._visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, visitors_count):
        if visitors_count > self.max_visitors_num:
            self._visitors_count = self.max_visitors_num
        else:
            self._visitors_count = self.visitors_count


Concert.max_visitors_num = 200
Concert.visitors_count = 2000
concert = Concert()
print(concert.visitors_count)


# 6.
@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


# 7
AddressBookDataClass = collections.namedtuple('AdressBookDataClass',
                                              ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])


# 8
class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

        def __str__(self):
            return f"(key: {self.key}, name: {self.name}, phone_number: {self.phone_number}, address: {self.address}, email: {self.email}, birthday: {self.birthday}, age: {self.age})"


# 9.
class Person:
    name = "John"
    age = 36
    country = "USA"


john = Person()
setattr(john, "age", 28)
print(getattr(john, 'age'))


# 10
class Student:
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(911, 'Volodymyr')
setattr(student, 'student_email', 'vk.iblogic@gmail.com')
print(getattr(student, 'student_email'))


class Celsius:

    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature_Fahrenheit(self):
        return (self._temperature * 1.8) + 32


print(Celsius(40).temperature_Fahrenheit)
