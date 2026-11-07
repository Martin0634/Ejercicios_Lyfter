print("---- EJERCICIOS EXTRA DE DICCIONARIOS - 3")

products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

total_by_category = {}

for i in range(len(products)):
    if products[i].get("category") not in total_by_category:
        total_by_category[products[i].get("category")] = 0
    total_by_category[products[i].get("category")] += products[i].get("price")

for i,j in total_by_category.items():
    print(f"{i}: {j}")