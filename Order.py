# Сущность заказа
class Order:
    # pizzas - список пицц, включенных в заказ
    def __init__(self, pizzas):
        self.pizzas = pizzas
        self.sum = 0

        for pizza in pizzas:
            self.sum += pizza.cost

    # Проверяет не пустой ли заказ
    def isEmpty(self):
        return len(self.pizzas) == 0
