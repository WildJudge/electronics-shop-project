import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

        self._name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)
        super().__init__()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            self._name = value[:10]
        else:
            self._name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = float(self.price * self.pay_rate)

    @classmethod
    def instantiate_from_csv(cls, filename):
        """Создает экземпляры класса Item из данных в CSV-файле"""

        # Очищаем список all перед загрузкой данных из CSV-файла
        cls.all = []

        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])

                existing_item = next((item for item in cls.all if item.name == name), None)
                if existing_item:
                    existing_item.price = price
                    existing_item.quantity = quantity
                else:
                    cls(name, price, quantity)

    @staticmethod
    def string_to_number(value):
        """Преобразует строку в число"""
        return float(value) if '.' in value else int(value)

    def __repr__(self):
        """Магический метод __repr__ для представления объекта в виде строки"""
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Магический метод __str__ для представления объекта в виде строки"""
        return self.name

    def __add__(self, other):
        """Позволяет сложить экземпляры класса Phone или Item по количеству товара в магазине"""
        if isinstance(other, Item):
            return self.quantity + other.quantity
