import asyncio
import time
from abc import ABC, abstractmethod

from Pizza import Pizza


def benchmark(func):
    def wrapper(self, *args, **kwargs):
        t = time.time()
        res = func(self, *args, **kwargs)
        print('\n[+]', func.__name__, ' - Время выполнения: {} секунд.'.format(time.time() - t), '\n')
        return res

    return wrapper


# Реализация пиццы барбекю
class BBQ(Pizza):
    def __init__(self):
        super().__init__()
        self.cost = 200
        self.ingredients = [
            "meat",
            "mayonnaise",
            "dough",
            "BBQ sauce"
        ]
        self.name = "BBQ"

    @benchmark
    async def cook(self):
        print("Making BBQ Pizza")

        for ingredient in self.ingredients:
            print(ingredient)
            # time.sleep(0.5)
            await asyncio.sleep(0.5)

        print("BBQ pizza is ready!")

