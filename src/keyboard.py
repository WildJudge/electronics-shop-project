from src.item import Item


class KeyboardMixin:
    """Миксин для изменения языка раскладки клавиатуры"""

    def __init__(self):
        self._language = "EN"

    def change_lang(self):
        """Метод для изменения языка раскладки клавиатуры"""
        if self._language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"

    @property
    def language(self):
        return self._language


class Keyboard(Item, KeyboardMixin):
    """Класс для представления товара 'клавиатура'"""

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def __repr__(self):
        return f"Keyboard('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name
