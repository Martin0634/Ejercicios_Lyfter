print("---- EJERCICIOS EXTRA DE SINTAXIS - 2")

sum = 0

for num in range(1,4):
    num = int(input("Digite un número: "))
    if num == 30:
        print("Correcto! Uno de los números es 30.")
        break
    else:
        sum += num

if num != 30 and sum != 30:
    print("Incorrecto. Ninguno de los números, ni la suma son 30.")
elif num != 30 and sum == 30:
    print("Correcto. La suma de los números es 30")