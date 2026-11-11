print("---- EJERCICIOS DE DICCIONARIOS - 2")

list_a = ['first_name', 'last_name', 'role']
list_b = ['Martin', 'Zeta', 'FullStack Developer']

my_new_dictionary = {}

for i in range(len(list_a)):
    my_new_dictionary[list_a[i]] = list_b[i]

for i,j in my_new_dictionary.items():
    print(f"{i}: {j}")