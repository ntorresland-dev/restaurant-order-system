from src.order import Order
from src.product import Product
from src.menu import Menu


products = [Product("completo", 2000),
            Product("papas fritas", 1300),
            Product("bebida", 990)]

menu = Menu(products)
order = Order()

completo = menu.get_product("completo")
order.add_product(completo)
papas_fritas = menu.get_product("papas fritas")
order.add_product(papas_fritas)

print(order)