class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = None
        self.pepperoni = None
        self.mushrooms = None
        self.onions = None
        self.bacon = None

    def __str__(self):
        return f"size: {self.size}\n" \
               f"cheese: {self.cheese}\n" \
               f"pepperoni: {self.pepperoni}\n" \
               f"mushrooms: {self.mushrooms}\n" \
               f"onions: {self.onions}\n" \
               f"bacon: {self.bacon}\n"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def set_cheese(self, cheese):
        self.pizza.cheese = cheese
        return self

    def set_pepperoni(self, pepperoni):
        self.pizza.pepperoni = pepperoni
        return self

    def set_mushrooms(self, mushrooms):
        self.pizza.mushrooms = mushrooms
        return self

    def set_onions(self, onions):
        self.pizza.onions = onions
        return self

    def set_bacon(self, bacon):
        self.pizza.bacon = bacon
        return self

    def get_pizza(self):
        return self.pizza


class PizzaDirector:
    def __init__(self):
        self.pizza = PizzaBuilder()

    def make_pizza(self, size: int = 18,
                   cheese: bool = True,
                   pepperoni: bool = True,
                   mushrooms: bool = True,
                   onions: bool = True,
                   bacon: bool = True):
        # Задаем все параметры кастомной пиццы.
        self.pizza.set_size(size)
        self.pizza.set_cheese(cheese)
        self.pizza.set_pepperoni(pepperoni)
        self.pizza.set_mushrooms(mushrooms)
        self.pizza.set_onions(onions)
        self.pizza.set_bacon(bacon)

    def get_pizza(self):
        return self.pizza.get_pizza()


pizza = PizzaDirector()
pizza.make_pizza(size=30,
                 cheese=True,
                 pepperoni=True,
                 mushrooms=True,
                 onions=False,
                 bacon=True)
print(pizza.get_pizza())
