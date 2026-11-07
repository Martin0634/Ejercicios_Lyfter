print("---- EJERCICIOS EXTRA DE ITERABLES Y LISTAS - 4")

my_list = [10,20,30,40,50,60,70]
new_list = []
sum = 0
avg = 0

for i in range(len(my_list)):
    sum += my_list[i]

avg = round(sum / len(my_list),2)

for i in range(len(my_list)):
    if my_list[i] > avg:
        new_list.append(my_list[i])

print(f"El promedio de la lista {my_list} es {avg}")
print(f"Los mayores al promedio son {new_list}")