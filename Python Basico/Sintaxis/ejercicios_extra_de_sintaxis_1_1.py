print("---- EJERCICIOS EXTRA DE SINTAXIS - 1")

price = float(input("Ingrese el precio del producto: $"))
discount = 0
final_price = 0

if price < 100:
    discount = price * 0.02
else:
    discount = price * 0.10

final_price = price - discount
print(f"El descuento del producto es ${round(discount,2)}")
print(f"El precio a pagar es de ${round(final_price,2)}")