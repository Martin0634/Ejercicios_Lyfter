class Product:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

class Inventory:
    def __init__(self):
        self.products_in_inventory = []
    
    def add_product(self, product):
        self.products_in_inventory.append(product)
        print("Product added.")
    
    def calculate_total_value_of_inventory(self):
        total_inventory = 0
        if not self.products_in_inventory:
            print(f"No products in inventory. Total inventory: ${total_inventory} ")
        else:
            for product in self.products_in_inventory:
                total_inventory += (product.price*product.qty)
            return total_inventory
    
    def show_all_products(self):
        if not self.products_in_inventory:
            print(f"No products in inventory.")
        else:
            print("Products in Inventory")
            for product in self.products_in_inventory:
                for keys, values in product.__dict__.items():
                    print(f"{keys}: {values}")
    
def main():
    inventory_1 = Inventory()
    inventory_1.calculate_total_value_of_inventory()
    product_1 = Product('Mouse', 5000, 3)
    inventory_1.show_all_products()
    inventory_1.add_product(product_1)
    inventory_1.show_all_products()
    print(f"Total inventory: ${inventory_1.calculate_total_value_of_inventory()}")
    product_2 = Product('Keyboard', 8000, 2)
    inventory_1.add_product(product_2)
    inventory_1.show_all_products()
    print(f"Total inventory: ${inventory_1.calculate_total_value_of_inventory()}")

if __name__ == '__main__':
    main()