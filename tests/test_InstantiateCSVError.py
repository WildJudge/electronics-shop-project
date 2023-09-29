import pytest
from src.item import Item, InstantiateCSVError


def test_instantiate_from_csv_file_not_found():
    """Проверяет, что исключение FileNotFoundError выбрасывается при отсутствии файла"""
    with pytest.raises(InstantiateCSVError) as excinfo:
        Item.instantiate_from_csv('non_existent_file.csv')
    assert str(excinfo.value) == "Отсутствует файл item.csv"


def test_instantiate_from_csv_corrupted_file():
    """Проверяет, что исключение InstantiateCSVError выбрасывается при поврежденном файле"""
    with pytest.raises(InstantiateCSVError) as excinfo:
        Item.instantiate_from_csv('src/corrupted_items.csv')
    assert str(excinfo.value) in ["Отсутствует файл item.csv", "Файл item.csv поврежден"]
