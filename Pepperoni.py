import asyncio
import time
from Pizza import Pizza


def benchmark(func):
    def wrapper(self, *args, **kwargs):
        t = time.time()
        res = func(self, *args, **kwargs)
        print('\n[+]', func.__name__, ' - Время выполнения: {} секунд.'.format(time.time() - t), '\n')
        return res

    return wrapper


# Реализация пиццы пеперони
class Pepperoni(Pizza):
    def __init__(self):
        super().__init__()
        self.ingredients = [
            "dough",
            "pepperoni",
            "ketchup",
            "cheese"
        ]
        self.cost = 250
        self.name = "Pepperoni"

    @benchmark
    async def cook(self):
        print("Making pepperoni pizza")

        for ingredient in self.ingredients:
            print(ingredient)
            # time.sleep(0.5)
            await asyncio.sleep(0.5)
        print("Pepperoni is ready!")
