from abc import ABC, abstractmethod


# Общий интерфейс
class Pizza(ABC):
    @abstractmethod
    def description(self) -> str: ...

    @abstractmethod
    def cost(self) -> float: ...


# Базовая пицца
class PlainPizza(Pizza):
    def description(self) -> str:
        return "Plain Dough & Sauce"

    def cost(self) -> float:
        return 5.0


# Базовый декоратор: хранит оборачиваемую пиццу
class ToppingDecorator(Pizza):
    name = ""
    price = 0.0

    def __init__(self, pizza: Pizza):
        self._pizza = pizza

    def description(self) -> str:
        return f"{self._pizza.description()}, {self.name}"

    def cost(self) -> float:
        return self._pizza.cost() + self.price


# Конкретные добавки
class Cheese(ToppingDecorator):
    name = "Cheese"
    price = 2.0


class Olives(ToppingDecorator):
    name = "Olives"
    price = 1.0


class Pineapple(ToppingDecorator):
    name = "Pineapple"
    price = 1.5


if __name__ == "__main__":
    pizza = PlainPizza()
    pizza = Cheese(pizza)
    pizza = Olives(pizza)
    pizza = Pineapple(pizza)

    print(f"Description: {pizza.description()}")
    print(f"Total cost: ${pizza.cost():.2f}")
