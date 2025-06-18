from abc import ABC, abstractmethod

class AbstractProduct(ABC):
    @abstractmethod
    def get_description(self):
        pass

class Product(AbstractProduct):
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        self.quantity = quantity
        if price > 0:
            self.__price = price
        else:
            raise ValueError('Цена не может быть меньше нуля!')

    @property
    def price(self):
        return self.__price

    @price.getter
    def get_price(self):
        return self.__price

    @price.setter
    def price(self,new_price):
        if new_price >= 0:
            self.__price = new_price
        else:
            raise ValueError('Новая цена не может быть нулевой')

    def get_description(self):
        pass

    def __add__(self, other):
        if isinstance(other, Product):
            new_quantity = self.quantity + other.quantity
            new_price = (self.__price * self.quantity + other.__price * other.quantity) / new_quantity
            return Product(f"{self.name} + {other.name}", new_quantity, new_price)
        else:
            raise TypeError("Можно складывать только объекты Product")

    def __lt__(self, other):
        if isinstance(other, Product):
            if self.__price < other.__price:
                return True
            else:
                return False
        else:
            raise TypeError("Можно сравнивать только объекты Product")

    def __gt__(self, other):
        if isinstance(other, Product):
            if self.__price > other.__price:
                return True
            else:
                return False
        else:
            raise TypeError("Можно сравнивать только объекты Product")

    def __str__(self):
        return f"{self.name} (Количество: {self.quantity}, Цена: {self.__price})"


class Book(Product):
    def __init__(self, name: str, quantity: int, __price: float, author: str):
        super().__init__(name, quantity, __price)
        self.name = name
        self.quantity = quantity
        self.author = author

    def __str__(self):
        return f"Книга: {self.name}, Автор: {self.author} (Количество: {self.quantity}, Цена: {self.__price})"

    def get_description(self):
        return f"Книга: {self.name}, Автор: {self.author}"


class Laptop(Product):
    def __init__(self, name: str, quantity: int, __price: float, brand: str):
        super().__init__(name, quantity, __price)
        self.brand = brand

    def __str__(self):
        return f"Ноутбук: {self.name}, Бренд: {self.brand} (Количество: {self.quantity}, Цена: {self.__price})"

    def get_description(self):
        return f"Ноутбук: {self.name}, Брэнд: {self.brand}"


try:
    invalid_book = Book("Ошибка наследования", 1, -100, "Автор")
    print(invalid_book)  # Цена -100 пройдет без ошибки!
    laptop = Laptop("Test", 1, 50000, "TestBrand")

except SyntaxError as e:
    print("Синтаксическая ошибка:", e)
except ValueError as e:
    print("Ошибка значения:", e)
