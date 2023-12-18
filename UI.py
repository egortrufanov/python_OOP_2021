import asyncio
from datetime import datetime

from peewee import *
from tkinter import *
from tkinter import messagebox
from functools import partial

from Customer import Customer
from Observer import Waiter
from Order import Order
from Pizzery import Pizzery

conn = SqliteDatabase('orders_history.db')


class BaseModel(Model):
    class Meta:
        database = conn


class OrderRecord(BaseModel):
    order_id = AutoField(column_name='OrderId')
    pizzas_count = IntegerField(column_name='PizzasCount')
    sum = IntegerField(column_name='Sum')
    date_time = DateTimeField(column_name='DateTime', default=datetime.now)

    class Meta:
        table_name = 'Orders'


class Window(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.grid()
        self.pizzery = Pizzery()
        self.client = Customer(1000.0)
        self.added_pizzas = []
        self.to_destroy = []

        self.balance_label = Label(self, text='Sum: ' + str(self.client.money))
        self.balance_label.grid(row=0, column=4)
        Label(self, text='Pizzas list').grid(row=1, column=0)
        self.order_label = Label(self, text='Order')
        self.order_label.grid(row=1, column=4)
        Button(self, text='Proceed order', command=self.do_tasks).grid(row=1, column=5)

        index = 2
        pizzas = [chef.prepare_pizza() for chef in self.pizzery.availableChefs]
        for pizza in pizzas:
            Label(self, text=pizza.name + '(' + str(pizza.cost) + ')', width=15).grid(column=0, row=index)
            Button(self, text="Add", command=partial(self.add_to_order, pizza)).grid(column=1, row=index)
            index += 1

    def add_to_order(self, pizza):
        self.added_pizzas.append(pizza)
        self.reset_order()

    def remove_from_order(self, pizza):
        self.added_pizzas.remove(pizza)

        for to_destroy in self.to_destroy:
            to_destroy.destroy()

        self.to_destroy.clear()

        self.reset_order()

    def reset_order(self):
        index = 2
        cost = 0
        for pizza in self.added_pizzas:
            cost += pizza.cost
            label = Label(self, text=pizza.name + '(' + str(pizza.cost) + ')')
            label.grid(row=index, column=4)
            button = Button(self, text='Delete', command=partial(self.remove_from_order, pizza))
            button.grid(row=index, column=5)
            index += 1

            self.to_destroy.append(label)
            self.to_destroy.append(button)

        self.order_label['text'] = 'Order (' + str(cost) + ')'

    def reset_balance(self):
        self.balance_label['text'] = 'Balance: ' + str(self.client.money)

    def do_tasks(self):
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(self.process_order())
        finally:
            return

    async def process_order(self):
        order = Order(self.added_pizzas)

        if order.isEmpty():
            messagebox.showinfo('Pizzeria', 'Order is empty')
        else:
            try:
                waiter = Waiter()
                self.pizzery.attach(waiter)
                await self.pizzery.getOrder(self.client, order)
                pizzas = waiter.pizzas

                if len(pizzas) != 0:
                    output = "Pizzas: \n"

                    for pizza in pizzas:
                        output += pizza.name + '\n'

                    messagebox.showinfo('Pizzeria', output)

                    count = len(pizzas)
                    order_record = OrderRecord(pizzas_count=count, sum=order.sum)
                    order_record.save()

                    order_read = OrderRecord.get(OrderRecord.order_id == order_record.order_id)
                    output = "Date: " + str(order_read.date_time) + "\n" + \
                             "Pizzas count: " + str(order_read.pizzas_count) + "\n" + \
                             "Sum: " + str(order_read.sum) + "\n"
                    messagebox.showinfo('Order saved', output)

                    self.reset_balance()
                    self.added_pizzas.clear()

                    for to_destroy in self.to_destroy:
                        to_destroy.destroy()

                    self.to_destroy.clear()
                    self.reset_order()


                else:
                    messagebox.showerror('Pizzeria', "Not enough money")
                    self.reset_balance()
                    self.added_pizzas.clear()
                    for to_destroy in self.to_destroy:
                        to_destroy.destroy()

                    self.to_destroy.clear()
                    self.reset_order()
            except Exception as ex:
                messagebox.showerror('Pizzeria', ex)
