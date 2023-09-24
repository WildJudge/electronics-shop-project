from src.keyboard import Keyboard


def test_keyboard_default_language():
    """Проверяет, что язык раскладки клавиатуры по умолчанию установлен в "EN"."""
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.language == "EN"


def test_keyboard_change_language():
    """Проверяет, что метод change_lang() изменяет язык раскладки клавиатуры на "RU"."""
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    assert kb.language == "RU"


def test_keyboard_toggle_language():
    """Проверяет, что метод change_lang() переключает язык раскладки клавиатуры между "EN" и "RU"."""
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang()  # EN -> RU
    kb.change_lang()  # RU -> EN
    assert kb.language == "EN"


def test_keyboard_repr():
    """Проверяет правильность работы метода __repr__() класса Keyboard"""
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert repr(kb) == "Keyboard('Dark Project KD87A', 9600, 5)"


def test_keyboard_str():
    """Проверяет правильность работы метода __str__() класса Keyboard"""
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
