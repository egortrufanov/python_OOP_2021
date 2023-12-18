from abc import ABC, abstractmethod
import Pizza
from BBQ import BBQ
from MonsterPizza import MonsterPizza
from Pepperoni import Pepperoni
from SeaSalad import SeaSalad

# Builder
class Chef(ABC):
    @abstractmethod
    def prepare_pizza(self) -> Pizza:
        pass

    @property
    def pizza_name(self) -> str:
        return self.prepare_pizza().name

    @property
    def pizza_cost(self) -> str:
        return self.prepare_pizza().cost


class BBQChef(Chef):
    def prepare_pizza(self) -> Pizza:
        return BBQ()


class PepperoniChef(Chef):
    def prepare_pizza(self) -> Pizza:
        return Pepperoni()


class SeaSaladChef(Chef):
    def prepare_pizza(self) -> Pizza:
        return SeaSalad()


class MonsterChef(Chef):
    def prepare_pizza(self) -> Pizza:
        return MonsterPizza()
