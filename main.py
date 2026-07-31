from src.order import Order
from src.product import Product


product1 = Product("Pizza", 2500)
product2 = Product("Bebida", 1100)
product3 = Product("Papas fritas", 2100)

order = Order()

order.add_product(product1)
order.add_product(product2)
order.add_product(product3)

total_price = order.get_total_price()
print(total_price)