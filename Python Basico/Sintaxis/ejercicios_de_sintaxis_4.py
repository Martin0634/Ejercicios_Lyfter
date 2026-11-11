print("---- EJERCICIO DE SINTAXIS - 4")
largest = 0

for number in range(1,4):
    number = int(input("Digite un número: "))
    if number > largest:
        largest = number

print(f"El número mayor es: {largest}")