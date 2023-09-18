class InvalidSalesItemError(Exception):
    def __init__(self, message: str) -> None:
        self._message = message

    def __repr__(self):
        return self._message


class MenuItem:
    """Create a Menu Item object with the name, cost, and selling price"""

    def __init__(self, name: str, wholesale_cost: float, selling_price: float) -> None:
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self) -> str:
        return self._name

    def get_wholesale_cost(self) -> float:
        return self._wholesale_cost

    def get_selling_price(self) -> float:
        return self._selling_price


class SalesForDay:
    """Create a SalesForDay object"""

    def __init__(self, days: int, sales_dict: dict) -> None:
        self._days = days
        self._sales_dict = sales_dict

    def get_day(self) -> int:
        return self._days

    def get_sales_dict(self) -> dict:
        return self._sales_dict


class LemonadeStand:
    """Create a LemonadeStand object"""

    def __init__(self, name: str) -> None:
        self._name = name
        self._day = 0
        self._menu = {}
        self._sales_record = []

    def get_name(self) -> str:
        return self._name

    def add_menu_item(self, menuItem: MenuItem):
        self._menu[menuItem.get_name()] = menuItem

    def enter_sales_for_today(self, sales_dict: dict):
        for item in sales_dict.keys():
            if item not in self._menu:
                raise InvalidSalesItemError("That item wasn't in the menu")
        salesForDay = SalesForDay(self._day, sales_dict)
        self._sales_record.append(salesForDay)
        self._day += 1

    def sales_of_menu_item_for_day(self, day: int, name: str) -> int:
        for item in self._sales_record:
            if item.get_day() == day:
                sales = item.get_sales_dict()
                if name in sales:
                    return sales[name]

        return "No information found for that day"

    def total_sales_for_menu_item(self, name: str) -> int:
        total_sales = 0
        for i in range(len(self._sales_record)):
            sales_for_day = self.sales_of_menu_item_for_day(i, name)
            if type(sales_for_day) == int:
                total_sales += sales_for_day
        return total_sales

    def total_profit_for_menu_item(self, name: str) -> float:
        total_sales = self.total_sales_for_menu_item(name)
        menuItem = self._menu[name]
        return total_sales * (
            menuItem.get_selling_price() - menuItem.get_wholesale_cost()
        )

    def total_profit_for_stand(self) -> float:
        total_profit = 0
        for item in self._menu.keys():
            total_profit += self.total_profit_for_menu_item(item)
        return total_profit


if __name__ == "__main__":
    # make Lemonade Stand object
    lemonade_stand = LemonadeStand("Megan's Lemonade Stand")

    # create menu items and add to lemonade stand
    basic_lemonade = MenuItem("Basic Lemonade", 1.0, 1.5)
    strawberry_lemonade = MenuItem("Strawberry Lemonade", 2.0, 3.0)
    sweet_lemonade = MenuItem("Sweet Lemonade", 1.50, 2.0)
    lemonade_stand.add_menu_item(basic_lemonade)
    lemonade_stand.add_menu_item(strawberry_lemonade)
    lemonade_stand.add_menu_item(sweet_lemonade)

    # create several dictionaries of items sold
    sales = {"Basic Lemonade": 20, "Strawberry Lemonade": 5, "Dog Water": 2}
    sales1 = {"Basic Lemonade": 15, "Strawberry Lemonade": 2, "Sweet Lemonade": 5}
    sales2 = {"Basic Lemonade": 12, "Strawberry Lemonade": 5, "Sweet Lemonade": 6}
    sales3 = {"Basic Lemonade": 25, "Strawberry Lemonade": 8, "Sweet Lemonade": 3}

    try:
        lemonade_stand.enter_sales_for_today(sales)
    except InvalidSalesItemError as e:
        print(e)

    try:
        lemonade_stand.enter_sales_for_today(sales1)
        lemonade_stand.enter_sales_for_today(sales2)
        lemonade_stand.enter_sales_for_today(sales3)
    except InvalidSalesItemError as e:
        print(e)

    total_profit = lemonade_stand.total_profit_for_stand()
    print(total_profit)
