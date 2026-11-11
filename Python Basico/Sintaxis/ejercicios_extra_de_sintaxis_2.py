print("---- EJERCICIOS EXTRA DE SINTAXIS - 2")

sum = 0

num_1 = int(input("Digite un número: "))
num_2 = int(input("Digite un número: "))
num_3 = int(input("Digite un número: "))

sum = num_1 + num_2 + num_3

if num_1 == 30 or num_2 == 30 or num_3 == 30:
    print("Correcto. Uno de los números es 30")
elif sum == 30:
    print("Correcto. La suma de los números es 30.")
else:
    print("Incorrecto. Ninguno de los números ni la suma son 30.")