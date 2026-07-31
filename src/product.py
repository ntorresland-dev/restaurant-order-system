class Product:
    # Represents a product of restaurant
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


    @property
    def price(self):
        return self.__price