from src.item import Item


class Phone(Item):
    """Класс для представления смартфона в магазине"""

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """Инициализация экземпляра класса Phone"""
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        """Магический метод для представления объекта Phone в виде строки"""
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
