from abc import ABC, abstractmethod


class InitLoggerMixin:
    def __init__(self, *args, **kwargs):
        class_name = self.__class__.__name__
        print(f"[InitLogger] Создан объект класса {class_name} с параметрами: args={args}, kwargs={kwargs}")
        super().__init__(*args, **kwargs)


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name, description, price, quantity):
        """Конструктор с базовыми параметрами товара."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @property
    @abstractmethod
    def price(self):
        """Геттер для получения цены"""
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        """Сеттер с проверкой: цена не может быть 0 или меньше"""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, data):
        """Класс-метод для создания продукта из словаря."""
        pass

    @abstractmethod
    def __str__(self):
        """Строковое отображение продукта"""
        pass

    @abstractmethod
    def add(self, other):
        """Сложение стоимости с другим товаром того же типа"""
        pass


class Product(InitLoggerMixin, BaseProduct):
    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.__price = price

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

    def add(self, other):
        """Сложение стоимости с другим товаром того же типа"""
        if not isinstance(other, Product):
            return NotImplemented
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных типов.")
        return self.price * self.quantity + other.price * other.quantity


class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.total_categories += 1
        Category.total_products += len(products)

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.total_products += 1
        else:
            print("Можно добавлять только товары (Product)")

    @property
    def products(self):
        """Геттер для получения списка товаров в читаемом виде."""
        result = []
        for p in self.__products:
            line = f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
            result.append(line)
        return result

    def __str__(self):
        product_list = "\n".join(self.products)
        return f"Категория: {self.name}\nОписание: {self.description}\nТовары:\n{product_list}"


class Smartphone(InitLoggerMixin, Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        base = super().__str__()
        return f"{base} | Модель: {self.model}, Память: {self.memory}, Цвет: {self.color}, Производительность: {self.efficiency}"


class LawnGrass(InitLoggerMixin, Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        base = super().__str__()
        return f"{base} | Страна: {self.country}, Срок прорастания: {self.germination_period}, Цвет: {self.color}"
