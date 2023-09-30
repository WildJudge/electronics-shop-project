import pytest
from src.item import Item, InstantiateCSVError
import os


def test_instantiate_from_csv_file_not_found():
    """Проверяет, что исключение FileNotFoundError выбрасывается при отсутствии файла"""
    with pytest.raises(FileNotFoundError) as excinfo:
        # Передаем несуществующий путь к файлу
        Item.instantiate_from_csv('non_existent_file.csv')
    assert str(excinfo.value) == "Отсутствует файл item.csv"


def test_instantiate_from_csv_corrupted_file():
    """Проверяет, что исключение InstantiateCSVError выбрасывается при поврежденном файле"""
    # Создаем поврежденный файл
    with open('corrupted_items.csv', 'w') as file:
        file.write("name,price,quantity\nСмартфон,100,1\nНоутбук,1000\nКабель,10,5\nМышка,50,5\nКлавиатура,75,5")

    with pytest.raises(InstantiateCSVError) as excinfo:
        # Передаем путь к поврежденному файлу
        Item.instantiate_from_csv('corrupted_items.csv')
    assert str(excinfo.value) == "Файл item.csv поврежден"

    # Удаляем временный файл
    os.remove('corrupted_items.csv')
