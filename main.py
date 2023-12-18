import asyncio
from tkinter import Tk

from Observer import Waiter
from Pizzery import Pizzery
from Customer import Customer
from UI import Window


async def start():
    client = Customer(1000)
    pizzery = Pizzery()

    while True:
        print("Баланс: " + str(client.money))
        print("Хотите сделать заказ? (+/-)")

        command = input()

        if command == "+":
            pizzery.showMenu()
            order = pizzery.createOrder()
            waiter = Waiter()
            pizzery.attach(waiter)
            await pizzery.getOrder(client, order)
        elif command == "-":
            break


if __name__ == '__main__':
    # asyncio.run(start())
    root = Tk()
    root.title("Пиццерия")
    root.geometry('450x200')
    calc = Window(root)
    root.mainloop()
