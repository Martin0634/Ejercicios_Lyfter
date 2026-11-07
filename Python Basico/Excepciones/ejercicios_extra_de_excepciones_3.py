def sum_list(list):
    total_sum = 0
    for i in range(len(list)):
        try:
            total_sum += float(list[i])
            print(f"{float(list[i])} sumado correctamente.")
        except ValueError as err:
            print(f"Elemento invalido: {list[i]}")
    print(f"Total de la suma: {total_sum}")


print("---- EJERCICIOS EXTRA DE EXCEPCIONES - 3 ----")
my_list = ['10', 'manzana', '5.5', '3', 'n/a']
sum_list(my_list)