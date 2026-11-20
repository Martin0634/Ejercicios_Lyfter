class Product:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

class Inventory:
    products_in_inventory = []
    
    def __init__(self):
        pass
    
    def add_product(self, product):
        Inventory.products_in_inventory.append(product)
        print("Product added.")
        input("")
    
    def calculate_total_value_of_inventory(self):
        total_inventory = 0
        if not Inventory.products_in_inventory:
            print(f"No products in inventory. Total inventory: ${total_inventory} ")
        else:
            for products in Inventory.products_in_inventory:
                total_inventory += (products.__dict__['price']*products.__dict__['qty'])
            print(f"Total inventory: ${total_inventory} ")
        input("")
    
    def show_all_products(self):
        if not Inventory.products_in_inventory:
            print(f"No products in inventory.")
        else:
            print("Products in Inventory")
            for products in Inventory.products_in_inventory:
                for keys, values in products.__dict__.items():
                    print(f"{keys}: {values}")
        input("")
    
def main():
    inventory_1 = Inventory()
    inventory_1.calculate_total_value_of_inventory()
    product_1 = Product('Mouse', 5000, 3)
    inventory_1.show_all_products()
    inventory_1.add_product(product_1)
    inventory_1.show_all_products()
    inventory_1.calculate_total_value_of_inventory()
    product_2 = Product('Keyboard', 8000, 2)
    inventory_1.add_product(product_2)
    inventory_1.show_all_products()
    inventory_1.calculate_total_value_of_inventory()

if __name__ == '__main__':
    main()