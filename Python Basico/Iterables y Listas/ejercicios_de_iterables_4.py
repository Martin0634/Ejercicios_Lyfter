print("---- EJERCICIOS DE ITERABLES Y LISTAS - 4")

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
i = 0

print (my_list)
while i != len(my_list):
    if my_list[i] % 2 != 0:
        my_list.pop(i)
        i -= 1
    i += 1

print(my_list)