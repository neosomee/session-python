from abc import ABC, abstractmethod

class AbstractProduct(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass


class Product(AbstractProduct):
    def __init__(self, name, quantity, price):
        if price < 0:
            raise ValueError("Цена не может быть меньше нуля!")
        self.name = name
        self.quantity = quantity
        self.price = price

    def __add__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        new_quantity = self.quantity + other.quantity
        new_price = ((self.price * self.quantity) + (other.price * other.quantity)) / new_quantity
        new_name = f"{self.name} + {other.name}"
        return self.__class__(new_name, new_quantity, new_price)

    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price

    def __gt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price > other.price

    def __str__(self):
        return f"{self.name} (Количество: {self.quantity}, Цена: {self.price:.2f})"

    def get_description(self) -> str:
        return f"Товар: {self.name}"


class Book(Product):
    def __init__(self, name: str, quantity: int, price: float, author: str):
        super().__init__(name, quantity, price)
        self.author = author

    def __str__(self):
        return f"Книга: {self.name}, Автор: {self.author} (Количество: {self.quantity}, Цена: {self.price:.2f})"

    def get_description(self) -> str:
        return f"Книга: {self.name}, Автор: {self.author}"


class Laptop(Product):
    def __init__(self, name: str, quantity: int, price: float, brand: str):
        super().__init__(name, quantity, price)
        self.brand = brand

    def __str__(self):
        return f"Ноутбук: {self.name}, Бренд: {self.brand} (Количество: {self.quantity}, Цена: {self.price:.2f})"

    def get_description(self) -> str:
        return f"Ноутбук: {self.name}, Бренд: {self.brand}"

try:
    book = Book("Война и мир", 5, 500, "Лев Толстой")
    book2 = Book("Преступление и наказание", 3, 450, "Фёдор Достоевский")

    print(book + book2)
    print(book > book2)
    print(book < book2)
    invalid_book = Book("Ошибка", 1, -100, "Автор")  # ValueError: Цена не может быть меньше нуля!
    print(book.get_description())

except SyntaxError as e:
    print("Синтаксическая ошибка:", e)
except ValueError as e:
    print("Отрицательное число:", e)