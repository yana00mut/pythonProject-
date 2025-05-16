class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для получения цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер с проверкой: цена не может быть 0 или меньше"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, data):
        """Класс-метод для создания продукта из словаря."""
        return cls(data["name"], data["description"], data["price"], data["quantity"])

    def __str__(self):
        """Строковое отображение продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):



# Класс Категория (Category)
class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.total_categories += 1

    def add_product(self, product):
        """Добавление объекта продукта в категорию."""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.total_products += 1
        else:
            print("Можно добавлять только товары (Product или его наследники)")

    @property
    def products(self):
        """Геттер для получения списка товаров в читаемом виде."""
        result = []
        for p in self.__products:
            line = f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
            result.append(line)
        return result
        return [str(p) for p in self.__products]

    def __str__(self):
