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
