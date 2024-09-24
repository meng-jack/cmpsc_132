class Food:
    """
        name -> str
        price_per_unit -> int/float

        >>> food_item_1 = Food('Donut', 1.5)
        >>> food_item_2 = Food('Scrambled Eggs', 2)
        >>> food_item_1.cost()
        1.5
        >>> food_item_2.cost()
        2
    """

    def __init__(self, name, price_per_unit):
        self.name = name
        self.price_per_unit = price_per_unit

    def cost(self):
        return self.price_per_unit

class Drink(Food):


class Snack(Food):


class Tray:
    """
        >>> food_item_1 = Food('Donut', 1.5)
        >>> food_item_2 = Food('Scrambled Eggs', 2)
        >>> my_breakfast = Tray()
        >>> my_breakfast.add_to_tray(food_item_1)
        >>> my_breakfast.add_to_tray(food_item_2)
        >>> my_breakfast.add_to_tray(food_item_1)
        >>> my_breakfast.add_to_tray(food_item_1)
        >>> my_breakfast.items
        [<Food object>, <Food object>, <Food object>, <Food object>]
        >>> my_breakfast
        Tray contents: Donut, Scrambled Eggs, Donut, Donut
    """

    def __init__(self):
        self.items = []

    def add_to_tray(self, food_item):
        self.items.append(food_item-)

    def __str__(self):
        str_repr = []
        for food_item in self.items:
            str_repr.append(food_item.name)
        return 'Tray contents: ' + ', '.join(str_repr)

    __repr__ = __str__
