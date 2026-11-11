print("---- EJERCICIOS EXTRA DE ITERABLES Y LISTAS - 3")

my_list = [9,4,7,1,5]
smallest = my_list[0]

for i in range(len(my_list)):
    if my_list[i] < smallest:
        smallest = my_list[i]

print(f"El número menor de la lista {my_list} es {smallest}")