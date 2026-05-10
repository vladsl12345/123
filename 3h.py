class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.price} грн)"


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product: Product):
        self.items.append(product)
        print(f"Додано: {product.name}")

    def remove_product(self, product: Product):
        if product in self.items:
            self.items.remove(product)
            print(f"Видалено: {product.name}")
        else:
            print("Такого товару немає в кошику.")

    def get_total_price(self):
        total = sum(product.price for product in self.items)
        return total

    def display_cart(self):
        print("\nВаш кошик:")
        for product in self.items:
            print(f" - {product.name}: {product.price} грн")
        print(f"Загальна вартість: {self.get_total_price()} грн\n")

laptop = Product("Ноутбук Dell", 35000.0)
mouse = Product("Миша", 800.0)

my_cart = Cart()

my_cart.add_product(laptop)
my_cart.add_product(mouse)
my_cart.add_product(mouse)

my_cart.display_cart()

my_cart.remove_product(mouse)

my_cart.display_cart()