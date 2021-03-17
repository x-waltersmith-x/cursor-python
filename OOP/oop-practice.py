import dataclasses
from abc import ABC, abstractmethod

VEGETABLES = ["Cocktail", 'Cherry']
FRUITS = ["Winter", 'Green']

states = {'nothing': 0, 'flowering': 1, 'green': 2, 'red': 3, 'rotten': 4}


class GardenMetaClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Garden(metaclass=GardenMetaClass):
    def __init__(self, vegetables, fruits, pests, gardener):
        self.vegetables = vegetables
        self.fruits = fruits
        self.pests = pests
        self.gardener = gardener

    def show_the_garden(self):
        print(f'The garden has such vegetables: {self.vegetables}')
        print(f'Also garden has such fruits: {self.fruits}')
        print(f'And such pests: {self.pests}')
        print(f'The maintainer of the garden is {self.gardener}')


@dataclasses.dataclass()
class PlantsStates:
    nothing: int
    flowering: int
    green: int
    red: int
    rotten: int


class Vegetables(ABC):
    def __init__(self, states, vegetable_type, name):
        self.states = states
        self.vegetable_type = vegetable_type
        self.name = name

    @property
    def vegetable_type(self):
        return self._vegetable_type

    @vegetable_type.setter
    def vegetable_type(self, vegetable_type):
        if vegetable_type in VEGETABLES:
            self._vegetable_type = vegetable_type
            print('all ok')
        else:
            raise Exception(f'There is no such a vegetable in the list. Your vegetable: {vegetable_type}')

    @abstractmethod
    def grow(self):
        raise NotImplementedError('Your method is not implemented.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError('Your method is not implemented.')


class Fruit(ABC):
    def __init__(self, states, fruits_type, name):
        self.states = states
        self.fruits_type = fruits_type
        self.name = name

    @property
    def fruits_type(self):
        return self._fruits_type

    @fruits_type.setter
    def fruits_type(self, fruits_type):
        if fruits_type in FRUITS:
            self._fruits_type = fruits_type
            print('all ok')
        else:
            raise Exception(f'There is no such a fruit in the list. '
                            f'Your fruit {fruits_type} and list {FRUITS}')

    @abstractmethod
    def grow(self):
        raise NotImplementedError('The method is missing.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError('The method is missing.')


