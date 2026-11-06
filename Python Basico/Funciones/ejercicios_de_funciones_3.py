def sum_list(my_list):
    total = 0
    for i in range(len(my_list)):
        total += my_list[i]
    return total

print("---- EJERCICIOS DE FUNCIONES - 3")
sample_list = [4,6,2,29]

total_list_sum = sum_list(sample_list)
print(f"La suma de los elementos de la lista es: {total_list_sum}")