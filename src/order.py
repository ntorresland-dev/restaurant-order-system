class Order:
    def __init__(self):
        self.__products = []
        self.__state = "PENDING"

    def add_product(self, product):
        self.__products.append(product)