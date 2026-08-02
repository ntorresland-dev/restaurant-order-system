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

    def confirm(self):
        if not self.__products:
            raise ValueError("El pedido no puede estar vacío, agrega por lo menos 1 producto.")

        if self.__state == "CONFIRMED":
            raise ValueError("El pedido ya ha sido confirmado.")

        self.__state = "CONFIRMED"

    def cancel(self):
        if self.__state == "CONFIRMED":
            raise ValueError("El pedido ya ha sido confirmado.")

        if self.__state == "CANCELLED":
            raise ValueError("El pedido ya ha sido cancelado.")

        self.__state = "CANCELLED"

    def __str__(self):
        products = "\n".join(f"- {product}" for product in self.__products)

        return ("Pedido\n"
                "Productos:\n"
                f"{products}\n"
                f"Precio Total: {self.get_total_price()}\n"
                f"Estado del pedido: {self.__state}"
        )