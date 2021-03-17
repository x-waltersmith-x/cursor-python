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


