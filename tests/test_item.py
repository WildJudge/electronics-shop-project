"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price():
    """Проверяет, что метод calculate_total_price правильно рассчитывает общую стоимость товара"""
    item = Item("Смартфон", 10000, 20)
    assert item.calculate_total_price() == 200000


def test_apply_discount():
    """Проверяет, что метод apply_discount правильно применяет скидку к цене товара"""
    item = Item("Смартфон", 10000, 20)
    item.pay_rate = 0.8
    item.apply_discount()
    expected_price = 8000.0
    assert item.price == expected_price


def test_apply_discount_with_custom_pay_rate():
    """
    Проверяет, что метод apply_discount правильно применяет скидку к цене товара
    с учетом пользовательской ставки скидки
    """
    Item.pay_rate = 0.9
    item = Item("Ноутбук", 20000, 5)
    assert item.price == 20000
    item.apply_discount()
    assert item.price == 18000.0


def test_all_items_list():
    """Проверяет, что созданные экземпляры товаров добавляются в список всех товаров"""
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1 in Item.all
    assert item2 in Item.all


def test_name_property_and_setter():
    """Проверяет геттер и сеттер для name."""
    item = Item("Смартфон", 10000, 20)
    assert item.name == "Смартфон"
    item.name = "СуперСмартфон"
    assert item.name == "СуперСмарт"


def test_instantiate_from_csv():
    """Проверяет метод instantiate_from_csv."""
    Item.all = []  # Очищаем список перед вызовом
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5


def test_string_to_number():
    """Проверяет метод string_to_number."""
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5.5
