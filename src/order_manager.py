class OrderManager:
    def __init__(self):
        self.__orders = []

    def add_order(self, order):
        self.__orders.append(order)

    def get_orders(self):
        return self.__orders

    def get_order(self, order_id):
        for order in self.__orders:
            if order_id == order.id:
                return order
        raise ValueError("Pedido no encontrado.")