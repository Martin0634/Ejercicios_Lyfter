print("---- EJERCICIOS EXTRA DE SINTAXIS - 4")

num = int(input("Digite un número del 1 al 10: "))
while num > 10 or num < 1:
    num = int(input("Fuera de rango. Digite un número del 1 al 10: "))

for times in range(1,12+1):
    print(f"{num} x {times} = {num * times}")