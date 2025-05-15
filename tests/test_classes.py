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