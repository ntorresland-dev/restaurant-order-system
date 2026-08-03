from src.order_manager import OrderManager
from src.order import Order
from src.product import Product
from src.menu import Menu


products = [Product("completo", 2000),
            Product("papas fritas", 1300),
            Product("bebida", 990)]

menu = Menu(products)

order = Order()


order.add_product(menu.get_product("completo"))
order.add_product(menu.get_product("papas fritas"))
order.add_product(menu.get_product("bebida"))

order2 = Order()
order2.add_product(menu.get_product("completo"))
order2.add_product(menu.get_product("bebida"))

order_manager = OrderManager()
order_manager.add_order(order)
order_manager.add_order(order2)

orders = order_manager.get_orders()

for order in orders:
    print(f"{order}\n")