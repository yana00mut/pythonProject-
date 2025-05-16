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


def test_set_price_ok():
    p = Product("Фломастер", "Красный", 20.0, 30)
    p.price = 30.0
    assert p.price == 30.0


def test_product_str():
    p = Product("Ластик", "Белый", 5.0, 10)
    assert str(p) == "Ластик, 5.0 руб. Остаток: 10 шт."
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
    assert str(s) in cat.products
def test_category_add_invalid_object(capfd):
    cat = Category("Разное", "Товары", [])
    cat.add_product("Не продукт")
    out, _ = capfd.readouterr()
    assert "Можно добавлять только товары" in out

def test_category_str():
    cat = Category("Овощи", "Свежие овощи", [])
    assert str(cat) == "Овощи (0 товаров)"
