from abc import abstractmethod, ABC

import Pizza
from Pizzery import Subject


class Observer(ABC):
    @abstractmethod
    def deliver_order(self, subject: Subject) -> None:
        pass


class Waiter(Observer):
    def __init__(self):
        super().__init__()
        self.pizzas = []

    def deliver_order(self, subject: Subject) -> None:
        self.pizzas = subject.ready_pizzas
        for pizza in subject.ready_pizzas:
            print("Клиент получил пиццу ", pizza.name)