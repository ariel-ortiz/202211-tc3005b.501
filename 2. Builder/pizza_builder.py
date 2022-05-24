# Ejemplo del patrón de Builder

from enum import Enum, auto
from typing import List


class Dough(Enum):
    ORIGINAL = auto()
    ITALIAN = auto()
    SKILLET = auto()
    CHEESE_STUFFED_EDGE = auto()
    CRUNCHY = auto()


class Size(Enum):
    MEDIUM = auto()
    LARGE = auto()
    CHOMPER = auto()


class Quantity(Enum):
    NONE = auto()
    REGULAR = auto()
    EXTRA = auto()


class Ingredient(Enum):
    JALAPENOS = auto()
    ONION = auto()
    OLIVES = auto()
    MUSHROOMS = auto()
    PEPPER = auto()
    PINEAPPLE = auto()
    HAM = auto()
    MANGO_HABANERO_SAUCE = auto()
    PARMESAN_CHEESE = auto()
    CREAM_CHEESE = auto()
    CHEDDAR_CHEESE = auto()
    SALAMI = auto()
    PEPPERONI = auto()
    CHORIZO = auto()
    GROUND_BEEF = auto()
    BACON = auto()
    CHICKEN = auto()


class Pizza:

    def __init__(self,
                 description: str,
                 dough: Dough,
                 size: Size,
                 sauce: Quantity,
                 cheese: Quantity,
                 ingredients: List[Ingredient]) -> None:
        self._description = description
        self._dough = dough
        self._size = size
        self._sauce = sauce
        self._cheese = cheese
        self._ingredients = ingredients

    def __str__(self):
        return (
f'''{self._description}
{'=' * len(self._description)}
- Dough: {self._dough.name.capitalize()}
- Size: {self._size.name.capitalize()}
- Sauce: {self._sauce.name.capitalize()}
- Cheese: {self._cheese.name.capitalize()}
- Ingredients: {(', '.join(i.name for i in self._ingredients)
                 if self._ingredients else 'None').title()}
''')

class PizzaBuilder:

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._description = 'Plain Cheese Pizza'
        self._dough = Dough.ORIGINAL
        self._size = Size.MEDIUM
        self._sauce = Quantity.REGULAR
        self._cheese = Quantity.REGULAR
        self._ingredients: List[Ingredient] = []

    def set_description(self, description: str) -> 'PizzaBuilder':
        self._description = description
        return self

    def set_dough(self, dough: Dough) -> 'PizzaBuilder':
        self._dough = dough
        return self

    def set_size(self, size: Size) -> 'PizzaBuilder':
        self._size = size
        return self

    def set_sauce(self, sauce: Quantity) -> 'PizzaBuilder':
        self._sauce = sauce
        return self

    def set_cheese(self, cheese: Quantity) -> 'PizzaBuilder':
        self._cheese = cheese
        return self

    def add_ingredient(self, ingredient: Ingredient) -> 'PizzaBuilder':
        self._ingredients.append(ingredient)
        return self

    def get_result(self) -> Pizza:
        return Pizza(
            self._description,
            self._dough,
            self._size,
            self._sauce,
            self._cheese,
            self._ingredients
        )


class HawaiianPizzaDirector:

    def __init__(self, builder: PizzaBuilder) -> None:
        self._builder = builder

    def make(self) -> Pizza:
        self._builder.reset()
        return (self._builder.set_description('Hawaiian Pizza')
            .set_size(Size.LARGE)
            .add_ingredient(Ingredient.PINEAPPLE)
            .add_ingredient(Ingredient.HAM)
            .get_result())


builder = PizzaBuilder()
director = HawaiianPizzaDirector(builder)
pizza = director.make()

print(pizza)
