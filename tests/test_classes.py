import pytest
from src.classes import Product, Category, Smartphone, LawnGrass


@pytest.fixture
def products():
    pen = Product("Ручка", "Синяя ручка", 10.0, 100)
    notebook = Product("Тетрадь", "96 листов", 25.0, 50)
    return [pen, notebook]


@pytest.fixture
def category(products):
    cat = Category("Канцелярия", "Школьные товары", products)
    return cat


def test_category_init(category):
    assert category.name == "Канцелярия"
    assert category.description == "Школьные товары"
    assert Category.total_categories == 1
    assert Category.total_products == 2


def test_create_product():
    p = Product("Карандаш", "Простой", 5.0, 80)
    assert p.name == "Карандаш"
    assert p.description == "Простой"
    assert p.price == 5.0
    assert p.quantity == 80


def test_new_product_method():
    data = {"name": "Скрепки", "description": "Металлические", "price": 3.5, "quantity": 100}
    p = Product.new_product(data)
    assert isinstance(p, Product)
    assert p.name == "Скрепки"


def test_set_price_ok():
    p = Product("Фломастер", "Красный", 20.0, 30)
    p.price = 30.0
    assert p.price == 30.0


def test_set_price_invalid(capfd):
    p = Product("Маркер", "Зеленый", 15.0, 10)
    p.price = -10
    out, _ = capfd.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in out
    assert p.price == 15.0  # цена не изменилась


def test_product_str():
    p = Product("Ластик", "Белый", 5.0, 10)
    assert str(p) == "Ластик, 5.0 руб. Остаток: 10 шт."


def test_product_add_not_product():
    p = Product("Товар", "Описание", 100, 2)
    with pytest.raises(TypeError):
        _ = p + "не продукт"


def test_add_products_same_class():
    p1 = Product("Товар1", "Описание", 100, 2)
    p2 = Product("Товар2", "Описание", 200, 3)
    assert p1 + p2 == 100 * 2 + 200 * 3


def test_add_products_different_classes_raises():
    s = Smartphone("iPhone", "Apple", 80000, 1, "высокая", "13 Pro", "128GB", "черный")
    g = LawnGrass("Газон", "Для дачи", 1000, 5, "Нидерланды", "7 дней", "зеленый")
    with pytest.raises(TypeError):
        _ = s + g


def test_category_add_valid_product():
    cat = Category("Техника", "Электроника", [])
    s = Smartphone("Samsung", "Galaxy", 50000, 2, "высокая", "S21", "256GB", "серый")
    cat.add_product(s)
    assert str(s) in cat.products_str_list()


def test_category_add_invalid_object(capfd):
    cat = Category("Разное", "Товары", [])
    cat.add_product("Не продукт")
    out, _ = capfd.readouterr()
    assert "Можно добавлять только товары" in out


def test_add_products_different_classes_raises():
    s = Smartphone("iPhone", "Apple", 80000, 1, "высокая", "13 Pro", "128GB", "черный")
    g = LawnGrass("Газон", "Для дачи", 1000, 5, "Нидерланды", "7 дней", "зеленый")
    with pytest.raises(TypeError):
        _ = s + g


def test_category_add_valid_product():
    cat = Category("Техника", "Электроника", [])
    s = Smartphone("Samsung", "Galaxy", 50000, 2, "высокая", "S21", "256GB", "серый")
    cat.add_product(s)
    assert str(s) in cat.products
    assert str(s) in [str(p) for p in cat._Category__products]


def test_category_add_invalid_object(capfd):
    cat = Category("Разное", "Товары", [])
    cat.add_product("Не продукт")
    out, _ = capfd.readouterr()
    assert "Можно добавлять только товары" in out


def test_category_str():
    cat = Category("Овощи", "Свежие овощи", [])
    expected = "Категория: Овощи\nОписание: Свежие овощи\nТовары:\n"
    assert str(cat) == expected


def test_init_logger_mixin_output(capfd):
    _ = Product("Продукт1", "Описание", 1200, 10)
    out, _ = capfd.readouterr()
    assert "Создан объект класса Product" in out
    assert "Продукт1" in out
    assert "1200" in out


def test_init_logger_smartphone_output(capfd):
    _ = Smartphone("iPhone", "Apple", 80000, 1, "высокая", "13 Pro", "128GB", "черный")
    out, _ = capfd.readouterr()
    assert "Создан объект класса Smartphone" in out
    assert "iPhone" in out


def test_init_logger_lawngrass_output(capfd):
    _ = LawnGrass("Газон", "Для дачи", 1000, 5, "Нидерланды", "7 дней", "зеленый")
    out, _ = capfd.readouterr()
    assert "Создан объект класса LawnGrass" in out
    assert "Газон" in out
    _ = Product("Продукт1", "Описание", 1200, 10)
    out, _ = capfd.readouterr()
    assert "Создан объект класса Product" in out
    assert "Продукт1" in out
    assert "1200" in out


def test_init_logger_smartphone_output(capfd):
    _ = Smartphone("iPhone", "Apple", 80000, 1, "высокая", "13 Pro", "128GB", "черный")
    out, _ = capfd.readouterr()
    assert "Создан объект класса Smartphone" in out
    assert "iPhone" in out


def test_init_logger_lawngrass_output(capfd):
    _ = LawnGrass("Газон", "Для дачи", 1000, 5, "Нидерланды", "7 дней", "зеленый")
    out, _ = capfd.readouterr()
    assert "Создан объект класса LawnGrass" in out
    assert "Газон" in out


def test_average_price_with_products(products):
    cat = Category("Канцелярия", "Школьные товары", products)
    expected_avg = sum(p.price for p in products) / len(products)
    assert cat.average_price() == expected_avg


def test_average_price_empty_category():
    cat = Category("Пустая категория", "Нет товаров", [])
    assert cat.average_price() == 0
