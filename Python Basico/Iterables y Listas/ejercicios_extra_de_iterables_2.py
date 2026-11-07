print("---- EJERCICIOS EXTRA DE ITERABLES Y LISTAS - 2")

my_list = [3,6,0,-2,4]
count = False

for i in range(len(my_list)):
    if my_list[i] <= 0:
        count = True

if count:
    print("Hay al menos un número negativo o cero.")
else:
    print("No hay números negativos ni ceros.")