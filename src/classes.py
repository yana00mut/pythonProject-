from abc import ABC, abstractmethod


class InitLoggerMixin:
    def __init__(self, *args, **kwargs):
        class_name = self.__class__.__name__
        print(f"[InitLogger] Создан объект класса {class_name} с параметрами: args={args}, kwargs={kwargs}")
        super().__init__(*args, **kwargs)


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name, description, price, quantity):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, data):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class Product(InitLoggerMixin, BaseProduct):
    def __init__(self, name, description, price, quantity):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.name = name
        self.description = description
        self.__price = None
        self.price = price  # через setter
        self.quantity = quantity

        super().__init__(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, data):
        return cls(data["name"], data["description"], data["price"], data["quantity"])

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только экземпляры Product или его подклассов.")
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных типов.")
        return self.price * self.quantity + other.price * other.quantity

    def add(self, other):
        return self + other


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        base = super().__str__()
        extra = f" | Модель: {self.model}, Память: {self.memory}, Цвет: {self.color}, Производительность: {self.efficiency}"
        return base + extra


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        base = super().__str__()
        return f"{base} | Страна: {self.country}, Срок прорастания: {self.germination_period}, Цвет: {self.color}"


class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = []
        for product in products:
            self.add_product(product)
        Category.total_categories += 1

    def add_product(self, product):
        if isinstance(product, Product):
            if product not in self.__products:
                self.__products.append(product)
                Category.total_products += 1
        else:
            print("Можно добавлять только товары (Product)")

    @property
    def products(self):
        return [str(p) for p in self.__products]

    def average_price(self):
        try:
            total_price = sum(p.price for p in self.__products)
            count = len(self.__products)
            return total_price / count
        except ZeroDivisionError:
            return 0

    def __str__(self):
        if not self.__products:
            product_lines = ""
        else:
            product_lines = '\n'.join(str(p) for p in self.__products)
        return f"Категория: {self.name}\nОписание: {self.description}\nТовары:\n{product_lines}"
