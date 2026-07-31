class Order:
    def __init__(self):
        self.__products = []
        self.__state = "PENDING"

    def add_product(self, product):
        self.__products.append(product)

    def get_total_price(self):
        total = 0

        for product in self.__products:
            total += product.price 

        return total