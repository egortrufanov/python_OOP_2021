# Сущность клиента (заказчика)
class Customer:
    # money - начальная сумма денег
    def __init__(self, money):
        self.__money__ = int(money)

    # sum стоимость заказа
    # pizzas список пицц
    # возвращает bool, удалась ли оплата
    def purchase(self, sum, pizzas):
        try:
            self.is_ready_to_spend(sum)
        except ReadyToSpendSomeMoney:
            self.__money__ -= sum
            print("Списание подтверждено")
            return True
        else:
            print("Недостаточно средств")
            return False

    # Получение баланса клиента
    @property
    def money(self):
        return self.__money__

    def is_ready_to_spend(self, sum):
        if self.money >= sum:
            raise ReadyToSpendSomeMoney(sum)
        else:
            return


class ReadyToSpendSomeMoney(Exception):
    def __init__(self, money):
        self.money = money

    def __str__(self):
        return "\nIm ready to spend " + repr(self.money) + "\n"
