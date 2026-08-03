class OrderManager:
    def __init__(self):
        self.__orders = []

    def add_order(self, order):
        self.__orders.append(order)

    def get_orders(self):
        return self.__orders