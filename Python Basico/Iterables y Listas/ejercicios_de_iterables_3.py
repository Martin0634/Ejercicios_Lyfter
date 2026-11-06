print("---- EJERCICIOS DE ITERABLES Y LISTAS - 3")

my_list = [4, 3, 6, 1, 7, 5, 2]
flag = my_list[0]
print(my_list)
my_list[0] = my_list[len(my_list)-1]
my_list[len(my_list)-1] = flag
print(my_list)
