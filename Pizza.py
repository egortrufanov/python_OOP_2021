import time
from abc import ABC, abstractmethod
import asyncio




# Базовый класс пиццы
class Pizza(ABC):
    def __init__(self):
        self.cost = 0
        self.ingredients = []
        self.name = 'Unknown'

    # Базовый метод приготовления пиццы
    @abstractmethod
    async def cook(self):
        print("Приготовление пиццы:")

        for ingredient in self.ingredients:
            print(ingredient)
        time.sleep(0.5)

        print("Пицца готова!")

    def __add__(self, other):
        if not isinstance(other, Pizza):
            raise TypeError

        resultPizza = Pizza()
        resultPizza.cost = self.cost + other.cost

        for ingredient in self.ingredients:
            resultPizza.ingredients.append(ingredient)

        for ingredient in other.ingredients:
            resultPizza.ingredients.append(ingredient)

        resultPizza.name = self.name + "-" + other.name

        return resultPizza
