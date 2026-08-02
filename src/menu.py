class Menu:
    def __init__(self, products):
        self.__products = products

    def get_products(self):
        return self.__products

    def get_product(self, product):
        for p in self.__products:
            if product.lower() == p.name.lower():
                return p
        raise ValueError("El producto no se encuentra disponible.")