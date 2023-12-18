import asyncio
from abc import ABC, abstractmethod
from threading import Thread
from typing import List

import Observer
import Pizza
from BBQ import BBQ
from Chef import SeaSaladChef, PepperoniChef, BBQChef, MonsterChef
from MonsterPizza import MonsterPizza
from Order import Order
from Pepperoni import Pepperoni
from SeaSalad import SeaSalad


def checker(func):
    def wrapper(self, customer, order):
        if order.isEmpty():
            return []
        else:
            return func(self, customer, order)

    return wrapper


class Greeter(type):
    def greetings(cls):
        print("\nWelcome to our Pizzery!!!\n")

    def __call__(self, *args, **kwargs):
        cls = type.__call__(self, *args)
        setattr(cls, "greetings", self.greetings)

        return cls


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


# Класс, работающий с консолью
class Pizzery(Subject):
    # Singleton
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Pizzery, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.availableChefs = [
            BBQChef(),
            PepperoniChef(),
            SeaSaladChef(),
            MonsterChef()
        ]

    # _observers: [Observer] = []
    # ready_pizzas: [Pizza] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.deliver_order(self)

    # Выводит меню в консоль
    def showMenu(self):
        for i in range(len(self.availableChefs)):
            print(i, ') ', self.availableChefs[i].pizza_name, ' - ', self.availableChefs[i].pizza_cost)

    # Создает заказ
    # Возвращает заказ
    def createOrder(self):
        print('Для заказа введите номера пицц через пробел:')
        inputted = input().split(' ')
        order = []

        for i in inputted:
            try:
                id = int(i)
                if id < 0 or id >= len(self.availableChefs):
                    print(str(id) + ' - некорректный номер')
                else:
                    order.append(self.availableChefs[id].prepare_pizza())
            except ValueError:
                print(str(i) + ' - не число')

        return Order(order)

    # Принимает заказ клиента
    # Возвращает список пицц
    @checker
    async def getOrder(self, customer, order):
        arr = [i.name for i in order.pizzas]
        confirm = customer.purchase(order.sum, arr)

        if confirm:
            for pizza in order.pizzas:
                await pizza.cook()
            self.ready_pizzas = order.pizzas
            self.notify()
        else:
            print("Отказ списания")
            await asyncio.sleep(0.1)
            return []



