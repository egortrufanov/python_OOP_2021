import asyncio
import time
from MusselRemoverMixin import MusselRemoverMixin
from Pizza import Pizza


def benchmark(func):
    def wrapper(self, *args, **kwargs):
        t = time.time()
        res = func(self, *args, **kwargs)
        print('\n[+]', func.__name__, ' - Время выполнения: {} секунд.'.format(time.time() - t), '\n')
        return res

    return wrapper


# Реализация морской пиццы
class SeaSalad(Pizza, MusselRemoverMixin):
    def __init__(self):
        super().__init__()
        self.ingredients = [
            "shrimps",
            "mussels",
            "dough",
            "mayonnaise"
        ]
        self.cost = 350
        self.name = "SeaSalad"

    @benchmark
    async def cook(self):
        print("Making sea salad")

        for ingredient in self.ingredients:
            print(ingredient)
            # time.sleep(0.5)
            await asyncio.sleep(0.5)
        print("Sea Salad pizza is ready!")
