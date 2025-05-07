import pytest
from src.classes import Product, Category

@pytest.fixture
def product_list():
    return [
        Product("Ручка", "Шариковая", 10.5, 100),
        Product("Тетрадь", "Клетка", 25.0, 50)
    ]

@pytest.fixture
def category(product_list):
    return Category("Канцелярия", "Товары для школы", product_list)

def test_product_initialization():
    product = Product("Карандаш", "Простой", 5.0, 80)
    assert product.name == "Карандаш"
    assert product.description == "Простой"
    assert product.price == 5.0
    assert product.quantity == 80

def test_category_initialization(category, product_list):
    assert category.name == "Канцелярия"
    assert category.description == "Товары для школы"
    assert category.products == product_list

def test_total_products_and_categories_reset():

    Category.total_categories = 0
    Category.total_products = 0

    p1 = Product("Линейка", "30см", 15.0, 20)
    p2 = Product("Циркуль", "Металлический", 45.0, 10)

    c1 = Category("Геометрия", "Инструменты", [p1])
    c2 = Category("Чертёж", "Инструменты", [p2])

    assert Category.total_categories == 2
    assert Category.total_products == 2
