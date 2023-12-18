import asyncio
import time
from BBQ import BBQ
from Pepperoni import Pepperoni


def benchmark(func):
    def wrapper(self, *args, **kwargs):
        t = time.time()
        res = func(self, *args, **kwargs)
        print('\n[+]', func.__name__, ' - Время выполнения: {} секунд.'.format(time.time() - t), '\n')
        return res

    return wrapper


# Реализация пиццы монстер
class MonsterPizza(Pepperoni, BBQ):
    def __init__(self):
        super().__init__()
        self.ingredients = [
            "double dough",
            "pepperoni",
            "ketchup",
            "cheese",
            "meat",
            "mayonnaise",
            "BBQ sauce"
        ]
        self.cost = 600
        self.name = "MonsterPizza"

    @benchmark
    async def cook(self):
        print("Making monster pizza")

        for ingredient in self.ingredients:
            print(ingredient)
            # time.sleep(0.5)
            await asyncio.sleep(0.5)
        print("MonsterPizza is ready!")
